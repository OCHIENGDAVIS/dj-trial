from django.urls import path

from .views import product_detail, product_home, product_create, ArticleListView, ArticleDetailView, ArticleCreateView

app_name = 'products'

urlpatterns = [

    path('', product_home, name='home'),
    path('<int:id>/', product_detail, name='detail'),
    path('create/', product_create, name='create'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/create', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:id>', ArticleDetailView.as_view(), name='articles_detail'),
]
