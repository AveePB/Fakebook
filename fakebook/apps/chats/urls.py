from django.urls import path
from apps.chats import views

# Create your tests here.
urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('messages/<str:user_uuid>/', views.ChatView.as_view(), name='message-page'),
]