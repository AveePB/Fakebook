from django.urls import path
from apps.settings import views

urlpatterns = [
    path('', views.SettingsRedirectView.as_view()),
    path('account-details/', views.AccountDetailsView.as_view(), name='account-details-page'),
]