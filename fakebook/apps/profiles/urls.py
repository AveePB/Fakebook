from django.urls import path
from apps.profiles import views

urlpatterns = [
    path('avatar/', views.AvatarView.as_view(), name='avatar-page'),
    path('background/', views.BackgroundView.as_view(), name='background-page'),
    path('bio/', views.BioView.as_view(), name='bio-page'),
    path('<str:user_uuid>/', views.ProfileView.as_view(), name='profile-page'),
    path('', views.ProfileRedirectView.as_view(), name='profile-redirect-page'),
]