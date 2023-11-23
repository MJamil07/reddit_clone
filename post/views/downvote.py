
from post.serializers.downvote import DownVoteSerializer
from post.models import UpVote , Post , DownVote
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from history.models import History
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_downvote(request):
    try:
        # * Get post id from request data
        post_id = request.data.get('post', None)
        
        post = get_object_or_404(Post , id = post_id)

        # * Check if the user has already upvoted  the post
        existing_vote = UpVote.objects.filter(upvoter=request.user, post=post_id).first()
        if existing_vote:
            existing_vote.delete()

        # * Create the downvote
        serializer = DownVoteSerializer(data={'downvoter': request.user.pk, 'post': post_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        History.objects.create(user=request.user , post = post , reason='downvote post')

        return Response({"detail": "Downvote created successfully."}, status=status.HTTP_201_CREATED)

    except Post.DoesNotExist:
        return Response({"detail": "Post does not exist."}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            