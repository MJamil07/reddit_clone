from django.db import models
from django.contrib.auth.models import User
from subreddits.models import Subreddit


class Post(models.Model):
      
      title = models.CharField(max_length=50)
      content = models.TextField()
      link = models.CharField(max_length=40 , null=True , blank=True)
      image = models.ImageField(upload_to = 'post/images/' , null = True , blank = True)
      video = models.FileField(upload_to='post/videos' , null = True , blank = True)
      created_at = models.DateTimeField(auto_now_add=True)

      author = models.ForeignKey(User, on_delete=models.CASCADE)
      subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE , null = True , blank = True)
      interest = models.CharField(max_length=30 , null = True , blank = True)
      
      POST_TYPES = [
        ('public', 'Public'),
        ('private', 'Private'),
      ]
      
      post_type = models.CharField(max_length=10, choices=POST_TYPES, default='public')
      
      def __str__(self):
            return f" [ title = {self.title} ] "
      
   
class UpVote(models.Model):
        
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      upvoter = models.ForeignKey(User, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)

      class Meta:
          unique_together = ['post', 'upvoter']

      def __str__(self):
          return f"[post={self.post.title}, upvoter={self.upvoter.username}]"


class DownVote(models.Model):
        
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      downvoter = models.ForeignKey(User, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)

      class Meta:
          unique_together = ['post', 'downvoter']

      def __str__(self):
          return f"[post={self.post.title}, downvoter={self.downvoter.username}]"