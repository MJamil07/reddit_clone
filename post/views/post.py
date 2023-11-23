from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from post.serializers.post import PostSerializer , ListPostSerializer
from post.models import Post
from subreddits.models import Subreddit
from myprofile.models import Connect
from rest_framework.response import Response
from rest_framework import status
from history.models import History

# * The CreatePost class is a generic view that allows for the creation of a new post.
class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request , *args , **kwargs):
            try:
                  serializer = self.get_serializer(data=request.data)
                  serializer.is_valid(raise_exception=True)
                  # Set the author of the post to the currently authenticated user
                  serializer.save(author=self.request.user)

                  # Get the subreddit ID from the request data
                  subreddit_id = self.request.data.get('subreddit', None)

                  # If a subreddit ID is provided, associate the post with the subreddit
                  if subreddit_id is not None:
                        subreddit = get_object_or_404(Subreddit, id=subreddit_id)

                        # Check if the user is a member of the subreddit
                        if not subreddit.members.filter(id=self.request.user.id).exists():
                              raise PermissionError("You are not a member of this subreddit.")

                        serializer.instance.subreddit = subreddit
                        serializer.save()

                  # Return a success response
                  return Response({'message': 'Post created successfully'}, status=status.HTTP_201_CREATED)

            except PermissionError as pe:
                  # Return a permission error response
                  return Response({'error': str(pe)}, status=status.HTTP_403_FORBIDDEN)

            except Exception as e:
                  # Return a generic error response
                  return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# * The DeletePost class is a generic view that allows for the deletion of a post.
class DeletePost(generics.DestroyAPIView):
      
      serializer_class = PostSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      
      def get_queryset(self): 
            return  Post.objects.filter(author=self.request.user)
      
      def perform_destroy(self , instance):
            instance.delete()
            

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])  
def list_post(request , *args , **kwargs):
      
      """  list the recently post user follower , following people and our community posts  """
      try:
            
            followers = Connect.objects.filter(following_user = request.user.id).values_list('user' , flat=True)
            followings = Connect.objects.filter(user = request.user.id).values_list('following_user' , flat = True)
            
            post_from_followers = Post.objects.filter(author__in=followers)
            post_from_followings = Post.objects.filter(author__in=followings)     
            
            subscribed_subreddit = Subreddit.objects.filter(members=request.user)
            posts_from_subreddits = Post.objects.filter(subreddit__in=subscribed_subreddit)

            all_posts = (post_from_followers | post_from_followings | posts_from_subreddits).order_by('-created_at')
            serializer = ListPostSerializer(all_posts, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

      
      except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrivePost(generics.RetrieveAPIView):
      """ all users allowed to retrieve all post """
      serializer_class = ListPostSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      queryset = Post.objects.all()
      
      def get(self , request , *args , **kwargs ):
            instance = self.get_object()
            # * create history when user is view the post 
            History.objects.create(user=request.user , post = instance , reason='view post')
            return super().get(request , *args , **kwargs) 
      
      