from apps.profiles.views import Profile
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.views import Response, status
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.
class HomePage(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Redirect unauthorized user
        if (request.user.is_anonymous):
            return redirect('hero-page')
        
        profile, created = Profile.objects.get_or_create(user=request.user)

        return render(request, 'bases/home.html', {
            'current_user_avatar_url': profile.get_avatar_url(),
            'current_user_uuid': profile.uuid, 
        })
