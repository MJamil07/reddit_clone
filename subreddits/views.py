from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from subreddits.serializers import SubredditSerializer
from subreddits.models import Subreddit
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from post.models import Post
from post.serializers.post import ListPostSerializer
from myprofile.serializers.connect import UserSerializer
from django.db.models import Count
from django.shortcuts import get_object_or_404

class CreateSubreddit(generics.CreateAPIView):
      """ create community for user """
      serializer_class = SubredditSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      queryset = Subreddit.objects.all()
      
      def perform_create(self , serializer):
            serializer.save(admin = self.request.user)
            subreddit_instance = serializer.instance  
            subreddit_instance.members.add(self.request.user)

class DestroySubreddit(generics.DestroyAPIView):
      """ delete the current user cummunity """
      
      serializer_class = SubredditSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      
      def get_queryset(self):
            return Subreddit.objects.filter(admin = self.request.user.id)
      

class GetCommunity(generics.RetrieveAPIView):
      """ get all community info like community recent posts , deatils , and members restrict for private community """
      serializer_class = SubredditSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      queryset = Subreddit.objects.all()
      
      def retrieve(self , request , *args , **kwargs):
            try:
                  subreddit = self.get_object()

                  # * Check if the user is a member if the subreddit is private
                  if subreddit.subreddit_type == 'private' and not subreddit.members.filter(id=request.user.id).exists():
                        return Response({'error': 'Access denied. You are not a member of this private subreddit.'},
                                    status=status.HTTP_403_FORBIDDEN)

                  # * Get all community posts
                  community_posts = Post.objects.filter(subreddit = subreddit.pk).order_by('-created_at')
                  post_serializer = ListPostSerializer(community_posts, many=True)

                  # * Retrieve subreddit info and members
                  serializer = self.get_serializer(subreddit)
                  data = serializer.data
                  data['posts'] = post_serializer.data
                  data['members'] = subreddit.members.all().values_list('username', flat=True)

                  return Response(data, status=status.HTTP_200_OK)

            except Subreddit.DoesNotExist:
                  return Response({'error': 'Subreddit does not exist'}, status=status.HTTP_404_NOT_FOUND)

            except Exception as e:
                  return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListSubreddits(generics.ListAPIView):
      """ list the all community based on most members """
      serializer_class = SubredditSerializer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]

      def get_queryset(self):
            return Subreddit.objects.annotate(num_members=Count('members')).order_by('-num_members')
      
      
      

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add_subreddit_members(request, *args, **kwargs):
      
      subreddit_id = request.data.get('subreddit', None)

      if subreddit_id is None:
            return Response({'error': 'Subreddit ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

      try:
            # * get subreddit object
            subreddit = Subreddit.objects.get(id=subreddit_id)

            # * if subreddt is private not allowed to add members 
            if subreddit.subreddit_type == 'private':
                  """ send mail to admin for approval ( Pending ) """
                  return Response({'error': 'This is a private subreddit. Not accessible.'}, status=status.HTTP_403_FORBIDDEN)

            user = request.user 

            # * check if user already member or not
            if subreddit.members.filter(id=user.id).exists():
                  return Response({'message': 'User is already a member of this subreddit'}, status=status.HTTP_200_OK)
      
            subreddit.members.add(user)
            return Response({'message': 'User added to subreddit members successfully'}, status=status.HTTP_201_CREATED)

      except Subreddit.DoesNotExist:
            return Response({'error': 'Subreddit does not exist'}, status=status.HTTP_404_NOT_FOUND)

      except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def remove_subreddit_members(request, *args, **kwargs):
      
      subreddit_id = request.data.get('subreddit', None)

      if subreddit_id is None:
            return Response({'error': 'Subreddit ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

      try:
            # * get subreddit object
            subreddit = Subreddit.objects.get(id=subreddit_id)
            
            user = request.user 

            # * check if user is not memeber
            if not subreddit.members.filter(id=user.id).exists():
                  return Response({'message': 'User is not a member of this subreddit'}, status=status.HTTP_400_BAD_REQUEST)

            # * unsubscribed subreddits
            subreddit.members.delete(user)
            return Response({'message': 'User added to subreddit members successfully'}, status=status.HTTP_201_CREATED)

      except Subreddit.DoesNotExist:
            return Response({'error': 'Subreddit does not exist'}, status=status.HTTP_404_NOT_FOUND)

      except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_community_members(request , subreddit_id , *args , **kwargs):
      
      try:
            # * Get subreddit object
            subreddit =  get_object_or_404(Subreddit , id = subreddit_id)
            
            # * get all members
            members = subreddit.members.all()
            
            # * serialize the data
            serialize = UserSerializer(members , many = True)
            return Response(serialize.data , status=status.HTTP_200_OK)
            
      except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def search_subreddits(request, *args, **kwargs):
      """ Basic search by community name and interest """
      
      try:
            result = None
            name_query = request.GET.get('name')
            interest_query = request.GET.get('interest')

            if name_query:
                  result = Subreddit.objects.filter(name__icontains=name_query)
            elif interest_query:
                  result = Subreddit.objects.filter(interest__icontains=interest_query)
            else:
                  result = Subreddit.objects.annotate(num_members=Count('members')).order_by('-num_members')

            serialized = SubredditSerializer(result, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)

      except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



            