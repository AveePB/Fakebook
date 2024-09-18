from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='notifications',
    )
    content = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.content[:20]}{'...' if len(self.content) > 20 else ''}"
    