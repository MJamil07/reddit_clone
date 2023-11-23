
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from history.serializer import HistorySerialzier
from history.models import History

"""
      when user view , upvote and downvote the post and comment history is created
"""

class DeleteOrGetHistory(generics.RetrieveDestroyAPIView):  
      """ Delete and retrieve history of authenticated user """
     
      serializer_class = HistorySerialzier
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      
      def get_queryset(self):
            return History.objects.filter(user=self.request.user.id)
      
class ListHistory(generics.ListAPIView):
      """ List the authentications user history recently created """
   
      serializer_class = HistorySerialzier
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      
      def get_queryset(self):
            return History.objects.filter(user=self.request.user.id).order_by('-create_at')
      
