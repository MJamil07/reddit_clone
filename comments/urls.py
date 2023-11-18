from django.urls import path
from . import views

urlpatterns = [
      path('create/' , views.create_comment , name = 'create comments'),
      path('delete/<int:pk>/' , views.DestroyComment.as_view() , name = 'delete comments'),
      path('update/<int:pk>/' , views.UpdateComment.as_view() , name = 'update comments'),
      path('upvote/' , views.upvote , name = 'upvote comments'),
      path('downvote/' , views.downvote , name = 'downvote comments'),
      
]