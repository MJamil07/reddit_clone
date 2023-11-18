from myprofile.models import Connect
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name')

class FollowersSerializer(serializers.ModelSerializer):
      
      user = UserSerializer()

      class Meta:
            model = Connect
            fields = ('user', )
            
class FollowingSerializer(serializers.ModelSerializer):
      
      following_user = UserSerializer()

      class Meta:
            model = Connect
            fields = ('following_user', )

class ConnectSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = Connect
            fields = '__all__'
