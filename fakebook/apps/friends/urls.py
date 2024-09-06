from django.urls import path
from apps.friends.views import FriendsView

urlpatterns = [
    path('', FriendsView.as_view(), name='friends'),
]