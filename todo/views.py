from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task

# Create your views here.
def task_list(request):
  task = Task.objects.all().order_by('-created_at')
  return render(request, 'todo/task_list.html', {'tasks':task})

def add_task(request):
  if request.method == 'POST':
    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()
    if title:
      Task.objects.create(
        title = title,
        description = description
        )
      return redirect(reverse('todo:task_list'))
    error = "title cannot be empty"
    return render(request, 'todo/task_form', {'error':error})
  return render(request, 'todo/task_form.html')  

def edit_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()
    completed = request.POST.get('completed') == 'on'
    if title:
      task.title = title
      task.description = description
      task.completed = completed 
      task.save()
      return render(reverse('todo/task_list.html'))
    return render(request, 'todo/task_form.html', {'tasks':task , 'error':"Title cannot be empty"})
  return render(request, 'todo/task_form.html', {'tasks':task})

def delete_task(request, pk):
  task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    task.delete()
    return redirect('todo:task_list')
  return render(request, 'todo/task_delete_confirm.html', {'task': task})

def toggle_task_complete(request, pk):
  task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    task.completed = not task.completed
    task.save()
  return redirect('todo:task_list')
