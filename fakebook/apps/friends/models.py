from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_initiated')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_received')

    class Meta:
        unique_together = ('user1', 'user2')
        # Optionally, enforce that the reverse relationship also can't exist
        constraints = [
            models.UniqueConstraint(fields=['user1', 'user2'], name='unique_friendship'),
            models.UniqueConstraint(fields=['user2', 'user1'], name='unique_reverse_friendship')
        ]

    def __str__(self):
        return f"Friendship between {self.user1} and {self.user2}"