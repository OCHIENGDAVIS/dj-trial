from django.urls import path
from .views import BookList, BookUpdate, BookDetail, BookDelete, BookCreate

app_name = 'cbv'

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('<int:id>/', BookDetail.as_view(), name='book_detail'),
    path('<int:id>/update/', BookUpdate.as_view(), name='book_update'),
    path('<int:id>/delete/', BookDelete.as_view(), name='book_delete'),
    path('create/', BookCreate.as_view(), name='book_create'),
]