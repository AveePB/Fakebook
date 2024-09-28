from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import Response, status
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import Http404

from apps.friends.models import Friendship
from apps.profiles.models import Profile
from apps.profiles.forms import *

# Create your views here.
class SettingsRedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Authentication check
        if (request.user.is_anonymous):
            return redirect('hero-page')
        return redirect('account-details-page')

class AccountDetailsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Authentication check
        if (request.user.is_anonymous):
            return redirect('hero-page')

        profile, created = Profile.objects.get_or_create(user=request.user)

        return render(request, 'settings/account_details.html', {
            'current_user_uuid': profile.uuid, 
            'current_user_avatar_url': profile.get_avatar_url(),
            'user': request.user,
        })

class ProfileDetailsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Authentication check
        if (request.user.is_anonymous):
            return redirect('hero-page')

        profile, created = Profile.objects.get_or_create(user=request.user)

        return render(request, 'settings/profile_details.html', {
            'current_user_uuid': profile.uuid, 
            'current_user_avatar_url': profile.get_avatar_url(),
            'user': request.user,
            'profile': profile,
        })

