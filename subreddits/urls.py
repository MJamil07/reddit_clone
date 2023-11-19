
from django.urls import path
from subreddits import views

urlpatterns = [
      path('create/' , views.CreateSubreddit.as_view() , name = 'create_community'),
      path('destroy/<int:pk>/' , views.DestroySubreddit.as_view() , name = 'destroy_community'),
      path('request_member/' , views.add_subreddit_members , name = 'request_member'),
      path('remove_member/' , views.remove_subreddit_members , name = 'remove_member'),
      path('get_community/<int:pk>/' , views.GetCommunity.as_view() , name = 'get_community'),
      path('list/' , views.ListSubreddits.as_view() , name = 'list_subreddits'),
      path('get_members/<int:subreddit_id>/' , views.get_community_members , name = 'get_community_members'),
      path('search/' , views.search_subreddits , name = 'search subreddits'),
      path('edit/<int:pk>/' , views.EditSubreddit.as_view() , name = 'Edit Subreddit'),
      path('get/<int:subredditId>/' , views.retrieve_community , name = 'Get Subreddit'),
]

