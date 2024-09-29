from django.urls import path
from apps.chats import views

# Create your tests here.
urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
]