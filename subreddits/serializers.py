
from rest_framework import serializers
from subreddits.models import Subreddit


class ListSubredditSerializer(serializers.ModelSerializer):
      class Meta:
            model = Subreddit
            exclude = ('admin' ,'members' , 'subreddit_type' , 'interest')

class SubredditSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = Subreddit
            exclude = ['admin']

class EditSubredditSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = Subreddit
            exclude = ('created_at' , 'admin' , 'members')