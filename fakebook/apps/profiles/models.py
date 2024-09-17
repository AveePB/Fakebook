from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
import datetime
import uuid

# Create your models here.
class Profile(models.Model):
    # Crucial data
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)

    # Updateable data
    last_active = models.DateTimeField(default=datetime.datetime.now)

    # Customizable data
    bio = models.TextField(max_length=256, default='...', null=False)
    avatar = models.ImageField(upload_to='avatars', default=None, null=False)
    background = models.ImageField(upload_to='backgrounds', default=None, null=False)

    def get_avatar_url(self):
        if (self.avatar):
            return self.avatar.url

        return settings.DEFAULT_AVATAR_URL
    
    def get_background_url(self):
        if (self.background):
            return self.background.url

        return settings.DEFAULT_BACKGROUND_URL

    def __str__(self) -> str:
        return f"User Profile {self.uuid}"