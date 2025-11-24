from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all().order_by('id')
    return render(request, 'board.html', {"tasks": tasks})



@login_required
def board_view(request):
    if request.method == "POST":
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST.get("description", ""),
            assignee_id=request.POST.get("assignee") or None,
            status="todo"
        )
        return redirect('board')

    context = {
        'todo': Task.objects.filter(status='todo'),
        'progress': Task.objects.filter(status='progress'),
        'done': Task.objects.filter(status='done'),
        'users': User.objects.all(),
    }
    return render(request, 'board/board.html', context)


@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get('status')
        if new_status in ['todo', 'progress', 'done']:
            task.status = new_status
            task.save()
    return redirect('board')


# API через DRF
from rest_framework import viewsets
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
