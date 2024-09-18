from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status
from django.shortcuts import render

from apps.notifications.models import Notification
from apps.profiles.models import Profile

# Create your views here.
class MarkNotificationAsSeen(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, notification_id):
        try:
            notification = Notification.objects.get(id=notification_id, user=request.user)
            notification.seen = True
            notification.save(force_update=True)

        except Notification.DoesNotExist:
            return Response({'message': 'Notification doesn\'t exist.'}, status.HTTP_404_NOT_FOUND)
        
        # Operation success
        return Response(None, status.HTTP_204_NO_CONTENT)

class ReadAllNotifications(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(user=request.user).order_by('-id')
        profile, created = Profile.objects.get_or_create(user=request.user)

        return render(request, 'bases/notifications.html', {
            'current_user_avatar_url': profile.get_avatar_url(),
            'current_user_uuid': profile.uuid,  
            'notifications': notifications
        })