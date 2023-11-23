from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from comments.models import Comment


class History(models.Model):
      
      user = models.ForeignKey(User , on_delete=models.CASCADE)
      post = models.ForeignKey(Post , on_delete=models.CASCADE , null=True , blank=True)
      comment = models.ForeignKey(Comment , on_delete=models.CASCADE , null=True , blank=True)
      
      REASON_CHOICES = (('upvote post' , 'Upvote a Post') , 
                        ('downvote post' , 'Downvote a Post') ,
                        ('view post' , 'View Post'),
                        ('comment post' , 'Comment Post'),
                        ('upvote comment' , 'Upvote Comment'),
                        ('downvote comment' , 'Downvote comment'),
                        ('view comment' , 'View Comment'))
      
      reason = models.CharField(max_length=30 , choices=REASON_CHOICES)
      create_at = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.reason
