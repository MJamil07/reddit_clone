
from rest_framework import serializers
from subreddits.models import Subreddit



class SubredditSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = Subreddit
            exclude = ['admin']

class EditSubredditSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = Subreddit
            exclude = ('created_at' , 'admin' , 'members')