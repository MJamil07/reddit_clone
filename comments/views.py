
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from comments.models import Comment
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from comments.serializers import CommentSerializer , ListCommentSerializer
from post.models import Post
from rest_framework import generics
from history.models import History


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_comment(request , *args , **kwargs):
      
      try:
            
            post_id = request.data.get('post')
            parent_comment_id = request.data.get('parent_comment')
            

            # * check if post exists are not
            post = get_object_or_404(Post, id=post_id)
            
            
            # * if parent comment is exists check object exists are not
            if parent_comment_id:
                  parent_comment = get_object_or_404(Comment, id=parent_comment_id)
            else:
                  parent_comment = None

            serializer = CommentSerializer(data=request.data)
            
            if serializer.is_valid():
                  # * create comment and save
                  serializer.save(user=request.user, post=post, parent_comment=parent_comment)
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      except Exception as e:
            return Response({'error' : str(e)} , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class DestroyComment(generics.DestroyAPIView):
      
      serializer_class = CommentSerializer
      permission_classes = [ IsAuthenticated ]
      authentication_classes = [ TokenAuthentication ]

      def get_queryset(self):
            return Comment.objects.filter(user = self.request.user.id)

class UpdateComment(generics.UpdateAPIView):
      
      serializer_class = CommentSerializer
      permission_classes = [ IsAuthenticated ]
      authentication_classes = [ TokenAuthentication ]

      def get_queryset(self):
            return Comment.objects.filter(user = self.request.user.id)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def upvote(request , *args , **kwargs): 
      
      try:
            comment_id = request.data.get('comment' , None)
            
            if comment_id is None:
                  return Response({'error' : 'Comment Does not Exists'} , status=status.HTTP_404_NOT_FOUND)
            
            comment = get_object_or_404(Comment , id = comment_id)
            comment.upvote(request.user)
            
            History.objects.create(user=request.user , comment = comment , reason= 'upvote comment')
            
            return Response({'message' : 'Upvoted'} , status=status.HTTP_200_OK)
            
      except Exception as e:
            return Response({'error' : str(e)} , status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def downvote(request , *args , **kwargs): 
      
      try:
            comment_id = request.data.get('comment' , None)
            
            if comment_id is None:
                  return Response({'error' : 'Comment Does not Exists'} , status=status.HTTP_404_NOT_FOUND)
            
            comment = get_object_or_404(Comment , id = comment_id)
            comment.downvote(request.user)
            
            History.objects.create(user=request.user , comment = comment , reason= 'downvote comment')
            
            return Response({'message' : 'Down voted'} , status=status.HTTP_200_OK)
            
      except Exception as e:
            return Response({'error' : str(e)} , status = status.HTTP_500_INTERNAL_SERVER_ERROR)
          


class RetriveComment(generics.RetrieveAPIView):
      
      serializer_class = ListCommentSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      queryset = Comment.objects.all()
      
      def get(self , request , *args , **kwargs):
            comment = self.get_object()
            History.objects.create(user=request.user , comment = comment , reason = 'view comment')
            return super().get(request , *args , **kwargs)