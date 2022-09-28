from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username
    todolist = Task.objects.filter(user=request.user)
    context = {
        'logged': username,
        'nama': 'Muhammad Hafizha Dhiyaulhaq',
        'npm' : '2106750723',
        'todolist': todolist,
    }
    return render(request, "todolist.html", context)


def create(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = request.POST["title"]
            description = request.POST["description"]
            user = request.user
            todo = Task(
                title=title,
                description=description,
                user=user,
                date=datetime.now())
            todo.save()
            return redirect('todolist:show_todolist')
    else:
        form = TaskForm()
    context = {'form':form}
    return render(request, 'create-task.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response

def set_task(request, pk):
    todolist = Task.objects.filter(pk=pk)
    if todolist.get().is_finished:
        todolist.update(is_finished=False)
    else:
        todolist.update(is_finished=True)
    return redirect('todolist:show_todolist')

def delete(request, pk):
    todolist = Task.objects.filter(pk=pk)
    todolist.delete()
    return redirect('todolist:show_todolist')

