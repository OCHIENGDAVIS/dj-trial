from django.urls import path

from .views import home, details, create, update, delete, user_profile, create_tag, create_comment

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('<int:id>', details, name='details'),
    path('<int:id>/comment/create', create_comment, name='create_comment'),
    path('<int:id>/update/', update, name='update'),
    path('<int:id>/delete', delete, name='delete'),
    path('create/', create, name='create'),
    path('<str:username>/', user_profile, name='user_profile'),
    path('tags/create', create_tag, name='create_tag'),
]
