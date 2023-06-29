from django.contrib import admin

from .models import Book, Floor, Shelf, Author

admin.site.register(Book)
admin.site.register(Floor)
admin.site.register(Shelf)
admin.site.register(Author)
