from apps.profiles.views import Profile
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import Response, status
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.http import Http404

from apps.profiles.models import Profile
from apps.friends.models import Friendship

# Create your views here.
class FriendsView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, user_uuid):
        # Check if not authenticated
        if (request.user.is_anonymous):
            return Response({'message': 'User is unauthorized.'}, status.HTTP_401_UNAUTHORIZED)

        try:
            # Safety check
            user_profile = Profile.objects.get(uuid=user_uuid)
            if (user_profile.user is request.user): return Response({'message': 'You cannot add yourself.'}, status.HTTP_409_CONFLICT)
    
            # Add new friend
            new_friendship = Friendship(user1=request.user, user2=user_profile.user)
            new_friendship.save(force_insert=True)

        except ValidationError:
            raise Http404()
        except Profile.DoesNotExist:
            raise Http404()
        except IntegrityError:
            return Response({'message': 'You already know this person.'}, status.HTTP_409_CONFLICT)

        # Operation success
        return Response({'message': 'Successfully met a new friend.'}, status.HTTP_201_CREATED)
    
    def delete(self, request, user_uuid):
        # Check if not authenticated
        if (request.user.is_anonymous):
            return Response({'message': 'User is unauthorized.'}, status.HTTP_401_UNAUTHORIZED)
        
        # Safety check
        try: 
            user_profile = Profile.objects.get(uuid=user_uuid)
        
        except Profile.DoesNotExist: 
            raise Http404()
        except ValidationError: 
            raise Http404()

        # Try to delete initiated friendship
        try:
            friendship = Friendship.objects.get(user1=request.user, user2=user_profile.user)
            friendship.delete()
        except:
            pass

        # Try to delete received friendship
        try:
            friendship = Friendship.objects.get(user1=user_profile.user, user2=request.user)
            friendship.delete()
        except:
            pass
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    def get(self, request, user_uuid):
        # Check if not authenticated
        if (request.user.is_anonymous):
            return redirect('hero-page')
        
        # Load user profile
        logged_user_profile, created = Profile.objects.get_or_create(user=request.user)
        try:
            # Get friendships
            user = Profile.objects.get(uuid=user_uuid).user
            friendships_initiated = [user.user2 for user in Friendship.objects.filter(user1=user)]
            friendships_received = [user.user1 for user in Friendship.objects.filter(user2=user)]
            
            # Concat lists
            friends = set()
            for friend in friendships_initiated: friends.add(Profile.objects.get(user=friend))
            for friend in friendships_received: friends.add(Profile.objects.get(user=friend))

        except ValidationError:
            raise Http404()
        except Profile.DoesNotExist:
            raise Http404()
    
        return render(request, 'bases/friends.html', {
                'current_user_avatar_url': logged_user_profile.get_avatar_url(),
                'current_user_uuid': logged_user_profile.uuid, 
                'friends': friends,
                'is_own': request.user == user,
            })