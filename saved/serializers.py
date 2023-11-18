from rest_framework import serializers
from saved.models import Saved
from post.serializers.post import ListPostSerializer
from comments.serializers import ListCommentSerializer

class SavedSerializers(serializers.ModelSerializer):
      
      post = ListPostSerializer()
      comment = ListCommentSerializer()
      
      class Meta:
            
            model = Saved
            fields = '__all__'
