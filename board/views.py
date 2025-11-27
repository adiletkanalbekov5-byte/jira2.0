from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Task


# ---------------------------
# Канбан доска (HTML)
# ---------------------------

@login_required
def board_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:  # защита от пустых задач
            Task.objects.create(
                title=title,
                description=request.POST.get("description", ""),
                assignee_id=request.POST.get("assignee") or None,
                status="todo",
                order=Task.objects.filter(status="todo").count()
            )
        return redirect('board')

    context = {
        'todo': Task.objects.filter(status='todo').order_by('order'),
        'progress': Task.objects.filter(status='progress').order_by('order'),
        'done': Task.objects.filter(status='done').order_by('order'),
        'users': User.objects.all(),
    }
    return render(request, 'board/board.html', context)


from django.http import HttpResponse
from django.template.loader import render_to_string

@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        new_status = request.POST.get('status')

        if new_status in ['todo', 'progress', 'done']:
            task.status = new_status
            task.order = Task.objects.filter(status=new_status).count()
            task.save()

            html = render_to_string("partials/task.html", {"task": task})
            return HttpResponse("OK")

    return HttpResponse("Ошибка", status=400)


# ---------------------------
# REST API (DRF)-----------

from rest_framework import viewsets, permissions
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('order')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
