
from myprofile.views import connect
from django.urls import path


urlpatterns = [
      
      path('follow/' , connect.create_connect , name = 'create_connect'),
      path('retrieve_followers/' , connect.RetrieveFollowers.as_view() , name = 'retrieve_followers'),
      path('retrieve_followings/' , connect.RetrieveFollowings.as_view() , name = 'retrieve_followings'),
      path('unfollow/' , connect.unFollow , name = 'unfollow')
      
]
                                                                                     
