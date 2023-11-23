from django.db import models
from django.contrib.auth.models import User
from post.models import Post

class Comment(models.Model):
      
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    upvotes = models.ManyToManyField(User, related_name='upvoted_comments', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvoted_comments', blank=True)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    
    def __str__(self):
        return f"Comment by {self.user.username} for {self.post} in {self.content}"

    def upvote(self, user):
        self.upvotes.add(user)
        self.downvotes.remove(user) if user in self.downvotes.all() else None

    def downvote(self, user):
        self.downvotes.add(user)
        self.upvotes.remove(user) if user in self.upvotes.all() else None
