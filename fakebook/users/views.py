from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from users.models import UserProfile
from users.forms import *
import os

# Create your views here.
class UsernameView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Create and process form
        form = UsernameForm(data=request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            user_id = request.user.id
            
            # Try to change username
            try:
                user = UserProfile.objects.get(id=user_id)
                user.username = username
                user.save(force_update=True)
                return Response({'message': 'Username successfully updated'}, status=201)
            except IntegrityError:
                return Response({'error': 'Username is alredy taken'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)            

class PasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Create and process form
        form = PasswordForm(data=request.POST)
        if (form.is_valid()):
            password = form.cleaned_data['password']
            user_id = request.user.id
            
            # Try to change password
            user = UserProfile.objects.get(id=user_id)
            user.password = password
            user.save(force_update=True)
            return Response({'message': 'Password successfully updated'}, status=201)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)        
    
class AvatarView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Check if there more than one file
        if (len(request.FILES) > 1):
            return Response({'error': 'Please upload exactly one image file.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create and process form
        form = AvatarForm(data=request.POST, files=request.FILES)
        if (form.is_valid()):
            avatar = form.cleaned_data['file']
            user_id = request.user.id
            
            # Delete previous avatar
            user = UserProfile.objects.get(id=user_id)
            try:
                if (user.avatar != None and os.path.exists(user.avatar.path)):
                    os.remove(user.avatar.path)
            except ValueError:
                pass
            
            # Try to change avatar
            user.avatar = avatar
            user.save(force_update=True)
            return Response({'message': 'Avatar successfully uploaded'}, status=201)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request):
        # Get user data
        user_id = request.user.id
        user = UserProfile.objects.get(id=user_id)

        # Delete current avatar
        try:
            if (user.avatar != None and os.path.exists(user.avatar.path)):
                os.remove(user.avatar.path)
        except ValueError:
            pass

        user.avatar = None
        user.save(force_update=True)

        return Response({'message': 'Avatar successfully deleted'}, status=201)         

class BioView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Create and process form
        form = BioForm(data=request.POST)
        if (form.is_valid()):
            bio = form.cleaned_data['bio']
            user_id = request.user.id
            
            # Try to change bio
            user = UserProfile.objects.get(id=user_id)
            user.bio = bio
            user.save(force_update=True)
            return Response({'message': 'Bio successfully updated'}, status=201)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)        