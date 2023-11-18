from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Connect(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
      following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

      class Meta:
            unique_together = ('user', 'following_user')

      def __str__(self):
            return f"[User {self.user.username} is following {self.following_user.username}]"


