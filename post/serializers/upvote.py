from rest_framework import serializers
from post.models import Post , UpVote

class UpVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpVote
        fields = ('post',)
