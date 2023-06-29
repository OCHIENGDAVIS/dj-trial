from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    shelf = models.ForeignKey('Shelf', on_delete=models.SET_NULL, null=True, blank=True)
    floor = models.ForeignKey('Floor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.title} By {self.author.name}'


class Shelf(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Floor(models.Model):
    number = models.IntegerField()
    shelves = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
