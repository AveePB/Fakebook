from django.urls import path
from apps.authz import views

urlpatterns = [
    path('register/', views.RegisterPage.as_view(), name='register-page'),
    path('login/', views.LoginPage.as_view(), name='login-page'),
]
