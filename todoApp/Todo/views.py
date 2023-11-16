from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .models import Task
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks })

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date'] + " " + request.POST['time']
        current_user = request.user
        user = User.objects.filter(username=current_user).first()

        if user:
            task = Task(title=title, description= description, date_valide=date ,user=user)
            task.save()
            messages.success(request, 'Task added successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Task')
            return redirect('home')
        
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        
        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        user = User(username=username, password=password)
        user.save()
        messages.success(request, 'User registered successfully.')
        return redirect('login')
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def update_data(request):
    print(request.POST)
    
    if request.method == 'POST':
        print(request.POST['task_id'])
        id = request.POST['task_id']
        id = id.replace('task_', '')
        task = Task.objects.filter(id=id).first()
        if task:
            task.delete()
            messages.success(request, 'Task completed successfully.')
            return redirect('home')
        else:
            return HttpResponse(request, 'Task does not exist.')