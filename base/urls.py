from django.urls import path

from .views import (home, rooms, detials, create_room, update_room, delete_room, delete_message, user_profile)

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('rooms/', rooms, name='rooms'),
    path('rooms/create', create_room, name='create_room'),
    path('users/profile/<str:pk>', user_profile, name='user_profile'),
    path('rooms/<str:pk>', detials, name='room_detail'),
    path('rooms/<str:pk>/update', update_room, name='update_room'),
    path('rooms/<str:pk>/delete', delete_room, name='delete_room'),
    path('rooms/<str:room_pk>/messages/<str:message_pk>/delete', delete_message, name='delete_message'),

]

