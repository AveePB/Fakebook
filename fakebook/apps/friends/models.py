from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

UserClass = get_user_model()

# Create your models here.
class Friendship(models.Model):
    user1 = models.ForeignKey(UserClass, related_name='friendships_created', on_delete=models.CASCADE)
    user2 = models.ForeignKey(UserClass, related_name='friendships_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')  # Ensures that the same friendship can't be created twice
        constraints = [
            models.CheckConstraint(check=~Q(user1=models.F('user2')), name='prevent_self_friendship')
        ]  # Prevents users from being friends with themselves

    def __str__(self):
        return f'Friendship between {self.user1} and {self.user2}'