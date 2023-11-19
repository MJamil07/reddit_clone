
from myprofile.views import connect
from django.urls import path
from myprofile.views import profile


urlpatterns = [
      
      path('follow/' , connect.create_connect , name = 'create_connect'),
      path('retrieve_followers/' , connect.RetrieveFollowers.as_view() , name = 'retrieve_followers'),
      path('retrieve_followings/' , connect.RetrieveFollowings.as_view() , name = 'retrieve_followings'),
      path('unfollow/' , connect.unFollow , name = 'unfollow'),
      
      path('update_profile/' , profile.UpdateProfile.as_view() , name = 'update profile'),
      path('retrieve_profile/<int:userId>/' ,profile.retrieve_profile , name = 'retrieve profile'),
      
]
                                                                                     
