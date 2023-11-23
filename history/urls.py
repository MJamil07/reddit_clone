
from django.urls import path
from history import views

urlpatterns = [
      path('list/' , views.ListHistory.as_view() , name = 'List History'),
      path('get_or_delete/' , views.DeleteOrGetHistory.as_view() , name = 'Delete or get the history')
]
