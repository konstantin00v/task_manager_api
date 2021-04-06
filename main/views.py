from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from rest_framework import generics
from .serializers import TaskDetailSerializer, TaskListSerializer
# Create your views here.

class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskDetailSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title':'Главная страница сайта', 'tasks': tasks })


def about(request):
    return render(request, 'main/about.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'


    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)