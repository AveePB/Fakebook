from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import Http404

from apps.profiles.models import Profile
from apps.profiles.forms import *
import uuid

# Create your views here.
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
    permission_classes = [IsAuthenticated]

    def get(self, request, user_uuid):
        current_user_profile, created = Profile.objects.get_or_create(user=request.user)
        current_user_avatar_url = current_user_profile.get_avatar_url()

        try:
            profile = Profile.objects.get(uuid=user_uuid)
            return render(request, 'bases/template.html', {
                'current_user_avatar_url': current_user_avatar_url,
                'current_user_uuid': current_user_profile.uuid, 
                'user': request.user, 
                'profile': profile,
            })
        except ValidationError:
            raise Http404()
        except Profile.DoesNotExist:
            raise Http404()