from django.urls import path
from apps.friends import views

urlpatterns = [
    path('<str:user_uuid>/', views.FriendsView.as_view(), name='friends-page'),
]