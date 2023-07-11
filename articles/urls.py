from django.urls import path
from .views import ArticleHomeView, SearchView


app_name = 'articles'

urlpatterns = [
    path('', ArticleHomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
]
