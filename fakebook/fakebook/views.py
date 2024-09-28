from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.views import Response, status
from django.db.models import Value
from django.db.models.functions import Concat

from apps.profiles.models import Profile

# Create your views here.
class HeroPage(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if (not request.user.is_anonymous):
            return redirect('home-page')
        
        return render(request, 'auth/hero.html')

class SearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        suggestions = []

        if (query):
            users = User.objects.annotate(
                    full_name=Concat('first_name', Value(' '), 'last_name')
                ).filter(full_name__icontains=query)[:10]  # Limit results to 10

            suggestions = [{
                'full_name': user.first_name + ' ' + user.last_name, 
                'avatar_url': Profile.objects.get(user=user).get_avatar_url(),
                'uuid': Profile.objects.get(user=user).uuid,
            } for user in users]

        return Response(suggestions, status.HTTP_200_OK)
        