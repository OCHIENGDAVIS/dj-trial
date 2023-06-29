from django.contrib import admin
from django.urls import path, include

from base.views import loginPage, logoutPage, registerPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('base.urls', namespace='base')),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logout'),
    path('products/', include('products.urls', namespace='products'))

]
