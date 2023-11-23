from post.serializers.upvote import UpVoteSerializer
from post.models import UpVote , Post , DownVote
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from history.models import History
from django.shortcuts import get_object_or_404


class CreateUpVote(generics.CreateAPIView):
      
      serializer_class = UpVoteSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
        
      queryset = UpVote.objects.all()

      def perform_create(self, serializer):
            
            try:
                  # * Get post id from request data
                  post_id = self.request.data.get('post', None)
                  
                  post = get_object_or_404(Post , id = post_id)

                  # * Check if the user has already downVote the post
                  existing_downvote = DownVote.objects.filter(downvoter=self.request.user, post=post_id).first()

                  # * upvote want create remove downvote one user vote only ones
                  if existing_downvote:
                        existing_downvote.delete()

                  #  *Create the upvote
                  serializer.save(upvoter=self.request.user, post=Post.objects.get(id = post_id))
                  
                  # * create history when upvote user
                  History.objects.create(user=self.request.user , post = post , reason='upvote post')
            
            except Exception as e:
                  return Response({'error' : e.with_traceback} , status=status.HTTP_500_INTERNAL_SERVER_ERROR )
            