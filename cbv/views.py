from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Book, Shelf, Author, Floor
from .forms import BookForm


class BookList(View):
    def get(self, request, *args, **kwargs):
        book_qs = Book.objects.all()
        shelve_qs = Shelf.objects.all()
        authors = Author.objects.all()
        floors = Floor.objects.all()
        ctx = {
            'books': book_qs,
            'shelves': shelve_qs,
            'authors': authors,
            'floors': floors
        }
        return render(request, 'cbv/book_list.html', ctx)


class BookDetail(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        obj = get_object_or_404(Book, id=id)
        ctx = {
            'book': obj
        }
        return render(request, 'cbv/book_detail.html', ctx)


class BookUpdate(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        book = get_object_or_404(Book, id=id)
        form = BookForm(instance=book)
        ctx = {
            'form': form,
            'book': book
        }
        return render(request, 'cbv/book_update.html', ctx)

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        book = get_object_or_404(Book, id=id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('cbv:book_detail', id=id)

        ctx = {'form': form, 'book': book}
        print(form.errors)
        return render(request, 'cbv/book_update.html', ctx)


class BookDelete(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        book = get_object_or_404(Book, id=id)
        ctx = {
            'book': book
        }
        return render(request, 'cbv/delete_confirm.html', ctx)

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        book = get_object_or_404(Book, id=id)
        book.delete()
        return redirect('cbv:book_list')


class BookCreate(View):
    def get(self, request, *args, **kwargs):
        form = BookForm()
        ctx = {
            'form': form
        }
        return render(request, 'cbv/book_create.html', ctx)

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cbv:book_list')
        ctx = {
            'form': form
        }
        return render(request, 'cbv/book_create.html', ctx)


