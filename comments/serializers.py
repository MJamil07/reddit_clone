

from rest_framework import serializers
from comments.models import Comment


class ListCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.replies.exists():
            return ListCommentSerializer(obj.replies.all(), many=True).data
        return None

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user' , )
