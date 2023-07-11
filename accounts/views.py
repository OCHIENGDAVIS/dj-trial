from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


class LogInView(View):
    def get(self, request):
        form = AuthenticationForm(request)
        ctx = {
            'form': form
        }
        return render(request, 'accounts/login.html', ctx)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('articles:home')

        ctx = {
            'form': form
        }
        return render(request, 'accounts/login.html', ctx)


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        print(dir(form))
        ctx = {
            'form': form
        }
        return render(request, 'accounts/create.html', ctx)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.data)
        ctx = {
            'form': form
        }
        return render(request, 'accounts/create.html', ctx)
