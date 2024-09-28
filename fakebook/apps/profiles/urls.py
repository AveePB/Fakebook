from django.urls import path
from apps.profiles import views

urlpatterns = [
    path('avatar/', views.AvatarView.as_view(), name='avatar-page'),
    path('background/', views.BackgroundView.as_view(), name='background-page'),
    path('bio/', views.BioView.as_view(), name='bio-page'),
    path('email/', views.EmailView.as_view(), name='email-page'),
    path('password/', views.PasswordView.as_view(), name='password-page'),
    path('first-name/', views.FirstNameView.as_view(), name='first-name-page'),
    path('last-name/', views.LastNameView.as_view(), name='last-name-page'),


    path('<str:user_uuid>/', views.ProfileView.as_view(), name='profile-page'),
    path('', views.ProfileRedirectView.as_view(), name='profile-redirect-page'),
]