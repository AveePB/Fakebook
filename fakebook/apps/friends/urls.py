from django.urls import path
from apps.friends.views import *

urlpatterns = [
    path('', FriendsView.as_view(), name='friends'),
    path('<int:user_id>/', FriendsView2.as_view(), name='friends2'),
]
