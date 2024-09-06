from django.urls import path
from apps.users.views import *

urlpatterns = [
    path('username/', UsernameView.as_view(), name='username'),
    path('password/', PasswordView.as_view(), name='password'),
    path('avatar/', AvatarView.as_view(), name='avatar'),
    path('bio/', BioView.as_view(), name='bio'),
]