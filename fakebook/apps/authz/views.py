from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import login
from django.db import IntegrityError
from django.shortcuts import render
from django.conf import settings

import datetime

from apps.users.forms import UsernamePasswordForm
from apps.users.models import UserProfile

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        form = UsernamePasswordForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        # Create and process form
        form = UsernamePasswordForm(data=request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check user credentials
            try:
                user = UserProfile.objects.filter(username=username, password=password).get()
                login(request, user)
                
                # Set up cookies
                response = Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
                token = AccessToken.for_user(user)

                response.set_cookie(
                    settings.SIMPLE_JWT['AUTH_COOKIE'],
                    str(token),
                    expires=datetime.datetime.now(datetime.UTC) + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    httponly=True,
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )

                return  response
            except UserProfile.DoesNotExist:
                return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # If form is invalid, return errors in response 
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        form = UsernamePasswordForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        # Create and process form
        form = UsernamePasswordForm(data=request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Try to save user
            try:
                new_user = UserProfile(username=username, password=password)
                new_user.save()
                return Response({'message': 'Registration successful.'}, status=status.HTTP_201_CREATED)
            except IntegrityError: 
                return Response({'error': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)
                
        # If form is invalid, return errors in response 
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)