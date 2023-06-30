from django.urls import path
from .views import BookList, BookUpdate, BookDetail, BookDelete, BookCreate, BookListGenericView, \
    BookListGenericDetailView, BookListGenericUpdateView

app_name = 'cbv'

urlpatterns = [

    path('<int:id>/', BookListGenericDetailView.as_view(), name='book_detail'),
    path('<int:id>/update/', BookListGenericUpdateView.as_view(), name='book_update'),
    path('<int:id>/delete/', BookDelete.as_view(), name='book_delete'),
    path('create/', BookCreate.as_view(), name='book_create'),
    path('', BookListGenericView.as_view(), name='book_list'),
]
