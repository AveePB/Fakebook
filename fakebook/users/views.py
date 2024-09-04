from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UsernameView(APIView):
    permission_classes = [IsAuthenticated]

class PasswordView(APIView):
    permission_classes = [IsAuthenticated]

class AvatarView(APIView):
    permission_classes = [IsAuthenticated]

class BioView(APIView):
    permission_classes = [IsAuthenticated]