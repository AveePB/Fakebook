from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from authz.models import UserCredentials
from django.contrib.auth import authenticate
from django.shortcuts import render

class IsUnauthenticated(BasePermission):
    """
    Allows access only to unauthenticated users.
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated
    
class LoginView(APIView):
    permission_classes = [IsUnauthenticated]

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # Examin request body
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username == None or password == None): return Response({"error": "Form is invalid"}, status=400)
        if (not username.isalnum() or len(username) > 32): return Response({"error": "Username doesn't meet the criteria"}, status=400)
        if (len(username) < 6 or len(username) > 32): return Response({"error": "Password doesn't meet the criteria"}, status=400)

        # Validate credentials
        user = UserCredentials.objects.filter(username=username)
        if (user.exists() and user.get().check_password(password)):
            refresh = RefreshToken.for_user(user.get())
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
        else:
            return Response({"error": "Invalid credentials"}, status=401)

# Create your views here.
class RegisterView(APIView):
    permission_classes = [IsUnauthenticated]

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # Examin request body
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username == None or password == None): return Response({"error": "Form is invalid"}, status=400)
        if (not username.isalnum() or len(username) > 32): return Response({"error": "Username doesn't meet the criteria"}, status=400)
        if (len(username) < 6 or len(username) > 32): return Response({"error": "Password doesn't meet the criteria"}, status=400)

        
        try:
            # Validate and create user
            user = UserCredentials(username=username)
            user.set_password(password)
            user.save(force_insert=True)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
        except Exception:
            return Response({"error": "User already exists"}, status=409)