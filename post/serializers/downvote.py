from rest_framework import serializers
from post.models import Post , DownVote

class DownVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownVote
        fields = ('post', 'downvoter')

   
