from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import BlogPost, Comment
from .forms import BlogForm, TagForm, CommentForm


def home(request):
    blogs = BlogPost.objects.all()
    ctx = {
        'blogs': blogs
    }
    return render(request, 'blog/index.html', ctx)


@login_required(login_url='login')
def details(request, id):
    msg = ''
    try:
        blog = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        msg = f'Blog post with ID "{id}" does ot exist'
    comments = Comment.objects.filter(blog_post=blog)
    form = CommentForm()
    ctx = {
        'blog': blog,
        'msg': msg,
        'form': form,
        'comments': comments
    }
    return render(request, 'blog/details.html', ctx)


@login_required(login_url='login')
def create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:home')
    ctx = {'form': form}
    return render(request, 'blog/create.html', ctx)


def update(request, id):
    msg = ''
    blog = None
    try:
        blog = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        msg = f' Blog post with id {id} does not exist'

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:details', id=blog.id)
        return redirect('blog:details', id=blog.id)
    form = BlogForm(instance=blog)
    ctx = {
        'blog': blog,
        'msg': msg,
        'form': form

    }
    return render(request, 'blog/update.html', ctx)


def delete(request, id):
    msg = ''
    blog = None
    try:
        blog = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        msg = f' Blog post with id {id} does not exist'

    if request.method == 'POST':
        blog.delete()
        return redirect('blog:home')
    ctx = {
        'blog': blog,
        'msg': msg

    }
    return render(request, 'blog/delete_confirm.html', ctx)


def user_profile(request, username):
    user = None
    msg = ''
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        msg = f'User with username {username} does not exist'
    user_posts = BlogPost.objects.filter(user=user)
    ctx = {
        'user': user,
        'msg': msg,
        'user_posts': user_posts
    }
    return render(request, 'blog/user_profile.html', ctx)


def create_tag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:create')
    print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'blog/create_tag.html', ctx)


def create_comment(request, id):
    if request.method == 'GET':
        return HttpResponse('Unsupported method')
    form = CommentForm(request.POST)
    if form.is_valid():
        blog = BlogPost.objects.get(id=id)
        comment = form.save(commit=False)
        comment.user = request.user
        comment.blog_post = blog
        form.save()
        return redirect('blog:details', id=blog.id)
    ctx = {}
    return render(request, 'blog/details.html', ctx)
