from django.shortcuts import render

from django.views import View
from.forms import ArticleForm


class SearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        if q is not None:
            print('Q is there')
        else:
            print('Q is no there')
        print(q)
        ctx = {}
        return render(request, 'articles/search_list.html', ctx)


class ArticleHomeView(View):

    def get(self, request):

        form = ArticleForm()
        ctx = {
            'form': form
        }
        return render(request, 'articles/home.html', ctx)

    def post(self, request):
        form = ArticleForm(request.POST)
        ctx = {
            'form': form
        }
        print(dir(form))
        return render(request, 'articles/home.html', ctx)



