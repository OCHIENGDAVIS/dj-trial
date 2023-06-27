from django.contrib import admin

from .models import Room, Topic, Message, Car, Manufacturer, Entry, Author, Blog
# Register your models here.

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(Blog)

