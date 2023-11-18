
from rest_framework import serializers
from subreddits.models import Subreddit



class SubredditSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = Subreddit
            exclude = ['admin']

