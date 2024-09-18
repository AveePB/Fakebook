from django.urls import path
from apps.notifications import views

urlpatterns = [
    path('mark/<int:notification_id>/', views.MarkNotificationAsSeen.as_view(), name='mark-notification'),
    path('', views.ReadAllNotifications.as_view(), name='read-notifications'),
]