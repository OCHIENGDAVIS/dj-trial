from django.urls import path

from .views import product_detail, product_home, product_create

app_name = 'products'

urlpatterns = [

    path('', product_home, name='home'),
    path('<int:id>/', product_detail, name='detail'),
    path('create/', product_create, name='create'),
]
