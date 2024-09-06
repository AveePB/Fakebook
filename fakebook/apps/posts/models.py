from django.contrib.auth import get_user_model
from django.db import models

UserClass = get_user_model()

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(UserClass, null=False, on_delete=models.CASCADE)
    content = models.TextField(max_length=600, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Post by {self.author.username}"