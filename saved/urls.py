from django.urls import path
from saved import views

urlpatterns = [
      path('create/' , views.create_saved , name = 'create saved'),
      path('unsaved/<int:pk>/' , views.UnSaved.as_view() , name = 'un  saved '),
      path('list/' , views.ListSaved.as_view() , name = 'list'),
]