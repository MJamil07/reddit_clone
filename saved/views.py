from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from comments.models import Comment
from saved.models import Saved
from django.shortcuts import get_object_or_404
from rest_framework import generics
from saved.serializers import SavedSerializers

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_saved(request , *args , **kwargs):
      
      try:
            post_id = request.data.get('post' , None)
            comment_id = request.data.get('comment' , None)
            
            # * check if post and comment is None or not
            if post_id is None and comment_id is None:
                  return Response({'message' : 'Post or Comment Expected'} , status=status.HTTP_400_BAD_REQUEST)
            
            if post_id is not None and comment_id is not None:
                  return Response({'message' : 'Post and Comment boths are exists'} , status = status.HTTP_400_BAD_REQUEST)
            
            if post_id is not None:
                  post = get_object_or_404(Post , id = post_id)
                  Saved.objects.create(post=post , comment=None , user=request.user).save()
                  
            elif comment_id is not None:
                  comment = get_object_or_404(Comment , id = comment_id)
                  Saved.objects.create(post=None , comment=comment , user = request.user)
            
            return Response({'message' : 'Successfully created saved'} , status=status.HTTP_200_OK)
            
      except Exception as e:
            return Response({'error' : str(e)} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UnSaved(generics.DestroyAPIView):
      
      serializer_class = SavedSerializers
      permission_classe = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      
      def get_queryset(self):
            return Saved.objects.filter(user=self.request.user.id)
      
      
      
      
class ListSaved(generics.ListAPIView):
      
      serializer_class = SavedSerializers
      permission_classe = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      

      def get_queryset(self):
            return Saved.objects.filter(user = self.request.user.id).order_by('-created_at')