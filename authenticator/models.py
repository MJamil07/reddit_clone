from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
          
    phone_number = models.CharField(max_length=15 , null = True , blank = True )  
    profile_photo = models.ImageField(upload_to = 'profile_photo/' , null = True , blank = True )
    karma = models.PositiveIntegerField(null = True , blank = True)
    interests = models.TextField(null=True, blank=True)
    social_links = models.TextField(null=True, blank=True)
    
    # * mapping by user
    user = models.OneToOneField(User , on_delete = models.CASCADE)

    def __str__(self):
              return f'[ user = {self.user.username} ]'

   