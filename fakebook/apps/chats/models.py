from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import uuid

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_author')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_recipient')
    content = models.TextField(default='')
    created_at = models.DateTimeField(default=datetime.now)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"Message from {self.author} to {self.recipient}"