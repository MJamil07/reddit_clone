from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from myprofile.models import Connect
from rest_framework import generics
from myprofile.serializers.connect import FollowersSerializer , FollowingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_connect(request, *args, **kwargs):
      try:
            # * Get following user id from request data
            following_user_id = request.data.get('following_user')

            # * Check if the current user is trying to follow themselves
            if request.user.id == following_user_id:
                  return Response({'message': 'Unwanted Connections'}, status=status.HTTP_400_BAD_REQUEST)

            # * Retrieve the following user instance if exist done else throw error
            following_user = User.objects.get(id=following_user_id)

            # * Create Connect instance
            connect_instance = Connect(user=request.user, following_user=following_user)
            connect_instance.full_clean() 
            connect_instance.save()

            return Response({'message': 'Connection created successfully'}, status=status.HTTP_201_CREATED)

      except User.DoesNotExist:
            return Response({'message': 'Following user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

      except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def unFollow(request , *args , **kwargs): 
      
      try:
            following_user_id = request.data.get('following_user' , None)
            
            if following_user_id is None:
                  return Response({'error' : 'Following User ID does not exists'} , status=status.HTTP_400_BAD_REQUEST)
            
            following_user = Connect.objects.filter(user=request.user.id , following_user=following_user_id).filter()
            
            if following_user.exists():
                  following_user.delete()
                  
            return Response({'message' : 'Sucessfully Unfollow'} , status=status.HTTP_200_OK)
            
      except Exception as e:
            return Response({'error' : str(e)} , status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class RetrieveFollowers(generics.ListAPIView):
      
      serializer_class = FollowersSerializer
      permission_classes = [ IsAuthenticated ]
      authentication_classes = [ TokenAuthentication ]
      
      def get_queryset(self):
            return Connect.objects.filter(following_user = self.request.user.id)
      
class RetrieveFollowings(generics.ListAPIView):
      
      serializer_class = FollowingSerializer
      permission_classes = [ IsAuthenticated ]
      authentication_classes = [ TokenAuthentication ]
      
      def get_queryset(self):
            return Connect.objects.filter(user = self.request.user.id)
      