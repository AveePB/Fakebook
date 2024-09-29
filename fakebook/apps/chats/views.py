from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import Response, status
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.http import Http404

from apps.profiles.views import Profile
from apps.friends.views import Friendship
from apps.chats.forms import MessageForm
from apps.chats.models import Message

# Create your views here.
class HomePage(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Redirect unauthorized user
        if (request.user.is_anonymous):
            return redirect('hero-page')
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        friends = []

        # Get users & profiles
        f_list = [f.user2 for f in Friendship.objects.filter(user1=request.user)]
        f_list2 = [f.user1 for f in Friendship.objects.filter(user2=request.user)]
        
        for f in f_list:
            p, created = Profile.objects.get_or_create(user=f)
            friends.append((f, p))

        for f in f_list2:
            p, created = Profile.objects.get_or_create(user=f)
            friends.append((f, p))

        return render(request, 'bases/home.html', {
            'current_user_avatar_url': profile.get_avatar_url(),
            'current_user_uuid': profile.uuid, 
            'friends_data': friends
        })

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_uuid):
        # Fetch user profiles
        try:
            author_profile, created = Profile.objects.get_or_create(user=request.user)        
            recipient_profile = Profile.objects.get(uuid=user_uuid)
        
        except ValidationError:
            return Http404()
        except Profile.DoesNotExist:
            return Http404()
        
        # Check if friends
        if (not (Friendship.objects.filter(user1=recipient_profile.user, user2=request.user).exists() or 
            Friendship.objects.filter(user1=request.user, user2=recipient_profile.user).exists())):
            return Response({'message': 'You aren\'t friends.'}, status.HTTP_409_CONFLICT)

        # Get messages
        author_messages = [(msg.content, msg.created_at) for msg in Message.objects.filter(author=request.user, recipient=recipient_profile.user).order_by('-created_at')]
        recipient_messages = [(msg.content, msg.created_at) for msg in Message.objects.filter(author=recipient_profile.user, recipient=request.user).order_by('-created_at')]

        return Response({   
            'author_avatar_url': author_profile.get_avatar_url(),
            'recipient_avatar_url': recipient_profile.get_avatar_url(),
            'author_messages': author_messages,
            'recipient_messages': recipient_messages,    
        }, status.HTTP_200_OK)

    def post(self, request, user_uuid):
        # Fetch user profiles
        try:
            author_profile, created = Profile.objects.get_or_create(user=request.user)        
            recipient_profile = Profile.objects.get(uuid=user_uuid)
        
        except ValidationError:
            return Http404()
        except Profile.DoesNotExist:
            return Http404()
        
        # Check if friends
        if (not (Friendship.objects.filter(user1=recipient_profile.user, user2=request.user).exists() or 
            Friendship.objects.filter(user1=request.user, user2=recipient_profile.user).exists())):
            return Response({'message': 'You aren\'t friends.'}, status.HTTP_409_CONFLICT)
        
        # Validate forms
        form = MessageForm(request.POST)
        if (form.is_valid()):
            msg_content = form.cleaned_data['content']
            
            # Save message
            new_msg = Message(content=msg_content, author=request.user, recipient=recipient_profile.user)
            new_msg.save(True)
            return Response(None, status.HTTP_204_NO_CONTENT)

        # Operation failed
        return Response(form.errors.as_text(), status.HTTP_400_BAD_REQUEST)