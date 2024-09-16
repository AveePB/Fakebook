from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.views import Response, status
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from apps.authz.forms import RegisterForm, LoginForm

# Create your views here.
class RegisterPage(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Check if authenticated
        if (not request.user.is_anonymous):
            return redirect('home-page')
        
        return render(request, 'auth/register.html')
    
    def post(self, request, *args, **kwargs):
        # Check if authenticated
        if (not request.user.is_anonymous):
            return redirect('home-page')
        
        # Validate POST data
        user_form = RegisterForm(request.POST)
        if (user_form.is_valid()):
            # Extract required data
            username = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']

            # Create new user
            try:
                created_user = User.objects.create_user(username, None, password, first_name=first_name, last_name=last_name)
                login(request, created_user)

                # Operation success
                return Response({'message': 'User has been created.'}, status.HTTP_201_CREATED)
            
            except IntegrityError:
                # Username is taken
                return Response({'message': 'Email is already registered.'}, status.HTTP_409_CONFLICT)

        # Invalid form
        return Response({'message': user_form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)
    
class LoginPage(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Check if authenticated
        if (not request.user.is_anonymous):
            return redirect('home-page')
        
        return render(request, 'auth/login.html')
    
    def post(self, request, *args, **kwargs):
        # Check if authenticated
        if (not request.user.is_anonymous):
            return redirect('home-page')
        
        # Validate POST data
        user_form = LoginForm(request.POST)
        if (user_form.is_valid()):
            # Extract required data
            username = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']

            # Check user credentials 
            authenticated_user = authenticate(request, username=username, password=password)
            if (authenticated_user):
                login(request, authenticated_user)

                # Operation success
                return Response({'message': 'User has been logged in.'}, status.HTTP_204_NO_CONTENT)
            
            # User data are invalid
            return Response({'message': 'Credentials are invalid.'}, status.HTTP_404_NOT_FOUND)

        # Invalid form
        return Response({'message': user_form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)