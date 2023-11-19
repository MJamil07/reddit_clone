
from rest_framework import serializers
from authenticator.models import CustomUser
from django.contrib.auth.models import User



class CustomUserSerialzer(serializers.ModelSerializer):
      class Meta:
            model = CustomUser
            exclude = ('user' , 'karma')

class UserSerializer(serializers.ModelSerializer):
      class Meta:
            model = User
            fields = ('first_name' , 'last_name' , 'username')
            