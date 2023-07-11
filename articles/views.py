from django.shortcuts import render
from django.db.models import Q

from django.views import View
from .forms import ArticleForm
from .models import Article


class SearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        articles = Article.objects.search(q)
        ctx = {
            'articles': articles
        }
        return render(request, 'articles/search_list.html', ctx)


class ArticleHomeView(View):

    def get(self, request):
        articles = Article.objects.all()

        ctx = {
            'articles': articles
        }
        return render(request, 'articles/home.html', ctx)

    def post(self, request):
        ctx = {

        }

        return render(request, 'articles/home.html', ctx)
