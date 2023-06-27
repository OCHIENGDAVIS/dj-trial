from django.shortcuts import render, redirect
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import RoomForm
from .models import Room, Topic, Message


# User = settings.AUTH_USER_MODEL this is s string and applicable is intances where you need a string


def home(request):
    return render(request, 'base/base.html')


def rooms(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_messages = Message.objects.all()

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': rooms.count(),
        'room_messages': room_messages
    }
    return render(request, 'base/rooms.html', context)


def detials(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')  # getting the child objects in a one to many r/ship
    participants = room.participants.all()
    if request.method == 'POST':
        Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('base:room_detail', pk=room.id)
    context = {
        'room': room,
        'msgs': room_messages,
        'participants': participants
    }
    return render(request, 'base/detail.html', context)


@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('base:rooms')
    return render(request, 'base/room_form.html', {'room_form': form})


@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('Not allowed, You are not owner')
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('base:room_detail', pk=room.id)
    return render(request, 'base/room_form.html', {'room_form': form})


@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('base:rooms')
    return render(request, 'base/delete.html', {'room': room})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('base:rooms')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('base:rooms')
        else:
            messages.error(request, 'Wrong Credentials , Try again')

    context = {}
    return render(request, 'base/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('base:rooms')


def registerPage(request):
    form = UserCreationForm()
    active_page = 'register'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                User.objects.get(username=request.POST.get('username'))
                messages.error(request, 'A user with that username already exists')
                return redirect('register')
            except User.DoesNotExist:
                user.username = user.username.lower()
                form.save()
                login(request, user)
                return redirect('base:rooms')
    return render(request, 'base/login_register.html',
                  {'form': form, 'active_page': active_page}

                  )


def delete_message(request, room_pk, message_pk):
    msg = Message.objects.get(id=message_pk)
    if request.user != msg.user:
        return HttpResponse('You do not have permission to delete the message')
    msg.delete()
    return redirect('base:room_detail', pk=room_pk)


def user_profile(request, pk):
    profile = User.objects.get(id=pk)
    rooms = profile.room_set.all()
    room_messages = profile.message_set.all()
    topics = profile.topic_set.all()
    context = {'profile': profile, 'roms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)
