from django.urls import path
from .views import *
urlpatterns = [
    path('',listMusic,name='music_list'),
    path('create/',createMusic.as_view(),name='music_create'),
]
