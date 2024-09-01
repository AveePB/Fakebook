from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from authz.models import UserCredentials
from django.shortcuts import render

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # Examin request body
        username = request.POST.get('username')
        password = request.POST.get('password')

        if (username == None or password == None): return Response({"error": "Form is invalid"}, status=400)
        if (not username.isalnum() or len(username) > 32): return Response({"error": "Username doesn't meet the criteria"}, status=400)
        if (len(password) < 6 or len(password) > 32): return Response({"error": "Password doesn't meet the criteria"}, status=400)

        # Validate credentials
        user = UserCredentials.objects.filter(username=username)
        if (user.exists() and user.get().check_password(password)):
            refresh = RefreshToken.for_user(user.get())
            return Response({'token': str(refresh.access_token)})
        else:
            return Response({"error": "Invalid credentials"}, status=401)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # Examin request body
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username == None or password == None): return Response({"error": "Form is invalid"}, status=400)
        if (not username.isalnum() or len(username) > 32): return Response({"error": "Username doesn't meet the criteria"}, status=400)
        if (len(password) < 6 or len(password) > 32): return Response({"error": "Password doesn't meet the criteria"}, status=400)

        try:
            # Validate and create user
            user = UserCredentials(username=username)
            user.set_password(password)
            user.save(force_insert=True)
            return Response({'message:', 'User successfully created'}, status=201)
        except Exception:
            return Response({"error": "User already exists"}, status=409)