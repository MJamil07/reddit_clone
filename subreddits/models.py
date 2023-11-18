from django.db import models
from django.contrib.auth.models import User

class Subreddit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField(null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_subreddits')
    members = models.ManyToManyField(User, related_name='subscribed_subreddits', blank=True)
    links = models.TextField(null=True, blank=True)
    rules = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to = 'subreddit/avatar' , null = True , blank = True)
    interest = models.TextField(null = True , blank = True)
    
    SUBREDDIT_TYPES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    
    subreddit_type = models.CharField(max_length=10, choices=SUBREDDIT_TYPES, default='public')

    def __str__(self):
        return f" {self.name} created by {self.admin.username}"
