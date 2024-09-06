from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.shortcuts import render
from django import forms

from apps.friends.models import Friendship

# Custom form
class UserIdForm(forms.Form):
    user_id = forms.IntegerField(
        min_value=0,
        max_value=2e9,
        required=True,
        error_messages={
            'required': 'Username is required.',
            'min_value': 'User id cannot be less than 0',
            'max_value': 'User id cannot exceed 2 000 000 000',
        }
    )

# Create your views here.
class FriendsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass