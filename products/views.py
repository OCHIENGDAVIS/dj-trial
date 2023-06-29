from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import Product, Article
from .forms import ProductForm, RawProductForm, ArticleForm


def product_home(request):
    products = Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request, 'products/home.html', ctx)


def product_detail(request, id):
    obj = Product.objects.get(id=id)
    ctx = {
        'obj': obj
    }
    return render(request, 'products/detail.html', ctx)


def product_create(request):
    form = ProductForm(request.POST or None)
    # form = RawProductForm(request.POST or None)
    if form.is_valid():
        # form.save()
        print(form.cleaned_data)
        return redirect('products:home')
    else:
        print(form.errors)
    print(form.errors)
    ctx = {'form': form}
    return render(request, 'products/create.html', ctx)


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'products/article_detail.html'
    # queryset = Article.objects.all()
    model = Article

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=id)


class ArticleCreateView(CreateView):
    template_name = 'products/article_create.html'
    model = Article
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
