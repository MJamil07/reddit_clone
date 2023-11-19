from django.db import models
from post.models import Post
from comments.models import Comment
from django.contrib.auth.models import User

class Saved(models.Model):
      """ Saved used to storing comment and post for current user """ 
      comment = models.ForeignKey(Comment , on_delete=models.CASCADE , blank=True , null=True)
      post = models.ForeignKey(Post , on_delete=models.CASCADE , null=True , blank=True)
      user = models.ForeignKey(User , on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            message = f"{self.user.username} is saved "
            if self.post is not None : message += f"post {self.post.title} "
            else:
                  message += f"comment {self.comment.content}"
                  
            return message
        