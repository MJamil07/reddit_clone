
from django.http import HttpRequest
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from myprofile.serializers.profile import UserSerializer , CustomUserSerialzer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from authenticator.models import CustomUser

class UpdateProfile(generics.UpdateAPIView):
      
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
                  
            except Exception as E:
                  return Response({'error' : str(e)} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

