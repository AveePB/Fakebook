from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import update_session_auth_hash
from rest_framework.views import Response, status
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import Http404
from django.db import IntegrityError

from apps.friends.models import Friendship
from apps.profiles.models import Profile
from apps.profiles.forms import *
import uuid

# Create your views here.
class EmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post (self, request, *args, **kwargs):
        form = EmailForm(request.POST)

        if (form.is_valid()):
            email = form.cleaned_data['email']
            try:
                request.user.username = email 
                request.user.save(force_update=True)
                
            except IntegrityError:
                return Response({'messsage': 'This email is already taken.'}, status.HTTP_409_CONFLICT)
                
            # Operation success
            return Response({'message': 'Email successfully updated.'}, status.HTTP_200_OK)

        # Invalid form
        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)        

# Create your views here.
class PasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post (self, request, *args, **kwargs):
        form = PasswordForm(request.POST)

        if (form.is_valid()):
            password = form.cleaned_data['password']
            request.user.password = password 
            request.user.save(force_update=True)
            update_session_auth_hash(request, request.user)
                            
            # Operation success
            return Response({'message': 'Password successfully updated.'}, status.HTTP_200_OK)

        # Invalid form
        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)        
    
class FirstNameView(APIView):
    permission_classes = [IsAuthenticated]

    def post (self, request, *args, **kwargs):
        form = FirstNameForm(request.POST)

        if (form.is_valid()):
            first_name = form.cleaned_data['first_name']
            request.user.first_name = first_name
            request.user.save(force_update=True)
                
            # Operation success
            return Response({'message': 'First name successfully updated.'}, status.HTTP_200_OK)

        # Invalid form
        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)        
    
class LastNameView(APIView):
    permission_classes = [IsAuthenticated]

    def post (self, request, *args, **kwargs):
        form = LastNameForm(request.POST)

        if (form.is_valid()):
            last_name = form.cleaned_data['last_name']
            request.user.last_name = last_name
            request.user.save(force_update=True)
                
            # Operation success
            return Response({'message': 'Last name successfully updated.'}, status.HTTP_200_OK)

        # Invalid form
        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)        

class AvatarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)

        if (form.is_valid()):
            avatar = form.cleaned_data['file']
            profile, created = Profile.objects.get_or_create(user=request.user)

            # Delete previous avatar
            if (not created): # If defined before
                profile.avatar.delete()
            
            # Generate custom name
            ext = avatar.name.split('.')[-1]
            new_filename = f"{uuid.uuid4().hex}.{ext}"
            
            # Try to change avatar
            profile.avatar.save(new_filename, avatar)
            profile.save(force_update=True)

            # Operation success
            return Response({'message': 'Avatar successfully uploaded.'}, status.HTTP_200_OK)

        # Invalid form
        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)        


    def delete(self, request, *args, **kwargs):
        profile, created = Profile.objects.get_or_create(user=request.user)
        
        if (not created): # If defined before
            profile.avatar.delete()
            profile.save(force_update=True)
        
        return Response(None, status.HTTP_204_NO_CONTENT)

class BackgroundView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)

        if (form.is_valid()):
            background = form.cleaned_data['file']
            profile, created = Profile.objects.get_or_create(user=request.user)

            # Delete previous background
            if (not created): # If defined before
                profile.background.delete()
            
            # Generate custom name
            ext = background.name.split('.')[-1]
            new_filename = f"{uuid.uuid4().hex}.{ext}"
            
            # Try to change background
            profile.background.save(new_filename, background)
            profile.save(force_update=True)

            # Operation success
            return Response({'message': 'Background successfully uploaded.'}, status.HTTP_200_OK)

        # Invalid form
        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)   

    def delete(self, request, *args, **kwargs):
        profile, created = Profile.objects.get_or_create(user=request.user)
        
        if (not created): # If defined before
            profile.background.delete()
            profile.save(force_update=True)
        
        return Response(None, status.HTTP_204_NO_CONTENT)

class BioView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Create and process form
        form = BioForm(request.POST)
        if (form.is_valid()):
            bio = form.cleaned_data['bio']
            
            # Try to change bio
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.bio = bio
            profile.save(force_update=True)
            
            return Response({'message': 'Bio successfully updated.'}, status.HTTP_200_OK)

        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_uuid):
        # Check if not authenticated
        if (request.user.is_anonymous):
            return redirect('hero-page')
        
        logged_user_profile, created = Profile.objects.get_or_create(user=request.user)
        logged_user_avatar_url = logged_user_profile.get_avatar_url()

        try:
            profile = Profile.objects.get(uuid=user_uuid)
            is_friend = (Friendship.objects.filter(user1=request.user, user2=profile.user).exists()
                or Friendship.objects.filter(user1=profile.user, user2=request.user).exists())
            
            return render(request, 'bases/profile.html', {
                'current_user_avatar_url': logged_user_avatar_url,
                'current_user_uuid': logged_user_profile.uuid, 
                'user': profile.user, 
                'profile': profile,
                'is_own': request.user == profile.user,
                'is_friend': is_friend,
            })
        except ValidationError:
            raise Http404()
        except Profile.DoesNotExist:
            raise Http404()
        
class ProfileRedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Check if not authenticated
        if (request.user.is_anonymous):
            return redirect('hero-page')
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        
        if created:
            profile.save()  # Save any additional modifications, if needed

        return redirect('profile-page', user_uuid=profile.uuid)
