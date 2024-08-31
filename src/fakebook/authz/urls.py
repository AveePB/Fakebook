from django.urls import path
from authz.views import LoginView, SignupView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
]