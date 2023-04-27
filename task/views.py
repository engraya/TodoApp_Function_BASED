from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TodoForm

# Create your views here.



def landingPage(request):
    return render(request, 'task/landingPage.html')


def home(request):
    tasks = Task.objects.all()
    
    context = {'tasks' : tasks}
    return render(request, 'task/homePage.html', context)


def createTask(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'task/homePage.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {'task' : task, 'form' : form}

    return render(request, 'task/updateTask.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("home")

    context = {'task' : task}

    return render(request, 'task/deleteTask.html', context)



