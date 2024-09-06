from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django import forms

# Create your views here.
class RecommendPostsView(APIView):
    permission_classes = [IsAuthenticated]

class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]

class RemovePostView(APIView):
    permission_classes = [IsAuthenticated]

class GetAllPostsView(APIView):
    permission_classes = [IsAuthenticated]
