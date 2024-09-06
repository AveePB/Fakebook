from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django import forms

from apps.users.models import UserProfile
from apps.friends.models import Friendship

# Custom form
class UserIdForm(forms.Form):
    user_id = forms.IntegerField(
        min_value=0,
        max_value=2e9,
        required=True,
        error_messages={
            'required': 'User id is required.',
            'min_value': 'User id cannot be less than 0.',
            'max_value': 'User id cannot exceed 2 000 000 000.',
        }
    )

# Create your views here.
class FriendsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        # Get all friends
        user = UserProfile.objects.get(id=request.user.id)
        
        # Get all friendships where the user is either user1 or user2
        friendships_created = Friendship.objects.filter(user1=user)
        friendships_received = Friendship.objects.filter(user2=user)
        
        # Combine both QuerySets to get all friends
        friends_from_created = [friendship.user2 for friendship in friendships_created]
        friends_from_received = [friendship.user1 for friendship in friendships_received]

        # Remove duplicates by converting to a set and then back to a list
        friends = list(set(friends_from_created + friends_from_received))

        # Return rightful template
        return render(request, 'editable_friend_list.html', {'user': request.user, 'friends': friends})

    def post(self, request, *args, **kwargs):
        # Create and validate form
        form = UserIdForm(data=request.POST)
        if (form.is_valid()):
            # Try to establish new friendship
            try:
                user_id = form.cleaned_data['user_id']
                user1 = UserProfile.objects.get(id=request.user.id)
                user2 = UserProfile.objects.get(id=user_id)

                new_friendship = Friendship(user1=user1, user2=user2)
                new_friendship.save(force_insert=True)

                return Response({'message': 'Successfully added a new friend.'}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'error': 'Failed to establish a new frienship.'}, status=status.HTTP_403_FORBIDDEN)
            except UserProfile.DoesNotExist:
                return Response({'error': 'User doesn\'t exist.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            # Send form error
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        
class FriendsView2(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        # Redirect if try to access logged user
        if (user_id == request.user.id):
            return redirect('/friends/')
        
        try:
            user = UserProfile.objects.get(id=user_id)
        
            # Get all friendships where the user is either user1 or user2
            friendships_created = Friendship.objects.filter(user1=user)
            friendships_received = Friendship.objects.filter(user2=user)
        
            # Combine both QuerySets to get all friends
            friends_from_created = [friendship.user2 for friendship in friendships_created]
            friends_from_received = [friendship.user1 for friendship in friendships_received]

            # Remove duplicates by converting to a set and then back to a list
            friends = list(set(friends_from_created + friends_from_received))

            # Return rightful template
            return render(request, 'friend_list.html', {'user': request.user, 'friends': friends})
        except UserProfile.DoesNotExist:
            return Response({'error': 'User doesn\'t exist.'}, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, user_id):
        # Try to delete friendship
        try:
            user1 = UserProfile.objects.get(id=request.user.id)
            user2 = UserProfile.objects.get(id=user_id)

            friendship = Friendship.objects.get(user1=user1, user2=user2)
            friendship.delete()

            return Response({'message': 'Successfully removed a friend.'}, status=status.HTTP_204_NO_CONTENT)
        except Friendship.DoesNotExist:
            return Response({'message': 'There was no friendship'}, status=status.HTTP_204_NO_CONTENT)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User doesn\'t exist.'}, status=status.HTTP_403_FORBIDDEN)
