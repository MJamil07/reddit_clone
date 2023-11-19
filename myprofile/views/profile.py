
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from django.http import HttpRequest
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from myprofile.serializers.profile import UserSerializer , CustomUserSerialzer , ListCustomUserSerialzer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from authenticator.models import CustomUser
from django.shortcuts import get_object_or_404
from myprofile.serializers.connect import FollowersSerializer
from post.models import Post
from post.serializers.post import ListPostSerializer
from comments.models import Comment
from comments.serializers import ListCommentSerializer
from myprofile.models import Connect

class UpdateProfile(generics.UpdateAPIView):
      """ update profile data for only authenticated user """
      serializer_class =  CustomUserSerialzer
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      
      def get_queryset(self):
            return CustomUser.objects.filter(user=self.request.user.id).first()
      
      def get_object(self):
            return CustomUser.objects.filter(user=self.request.user.id).first()
            
      def update(self , request : HttpRequest):
            try:
                  user_data = request.data.pop('user' , {})
                  custom_user_instance = self.get_object()
                  custom_user_serializer = self.get_serializer(custom_user_instance , data = request.data , partial = True)
                  custom_user_serializer.is_valid(raise_exception=True)
                  custom_user_serializer.save()

                  user_instance = self.request.user
                  user_serializer = UserSerializer(user_instance, data=user_data, partial=True)
                  user_serializer.is_valid(raise_exception=True)
                  user_serializer.save()

                  return Response(custom_user_serializer.data, status=status.HTTP_200_OK)
                  
            except Exception as e:
                  return Response({'error' : str(e)} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def retrieve_profile(request : HttpRequest , userId : int ,  *args , **kwargs):
      """ Retrieve the user profiles informations like post , comments , followers , aboat , user data """
      try:
            profile = {}
            # * Retrieve the user informations
            user = get_object_or_404(CustomUser , id = userId)
            user_info = ListCustomUserSerialzer(user).data
            profile['user'] = user_info
            
            # * Retrieve the user followers
            followers = Connect.objects.filter(following_user = user.user)
            print(followers)
            followers_info = FollowersSerializer(followers , many = True).data
            profile['followers'] = followers_info
            
            # * Retrieve the user post
            posts = ListPostSerializer(Post.objects.filter(author=user.user) , many = True).data
            profile['posts'] = posts
            
            # * Retrieve the user comments
            comments = ListCommentSerializer(Comment.objects.filter(user=user.user) , many = True).data
            profile['comments'] = comments
            
            return Response(profile , status=status.HTTP_200_OK)
            
      except Exception as e:
                  return Response({'error' : str(e)} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
