

from django.urls import path
from post.views import post , upvote , downvote

urlpatterns = [
      
      # * post endpoint
      path('create_post/' , post.CreatePost.as_view() , name = 'create_post'),
      path('delete_post/<int:pk>/' , post.DeletePost.as_view() , name = 'delete_post'),
      path('list_post/' , post.list_post , name = 'list_post'),
      
      # * upvote endpoint
      path('create_upvote/' , upvote.CreateUpVote.as_view() , name = 'create_upvote'),
      
      # * downvote endpoint
      path('create_downvote/' , downvote.create_downvote , name = 'create_downvote')
]
