from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    content_object_name = 'task1'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'Details.html'
    content_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def get_successurl():
    return reverse_lazy('cbvDetails', kwargs={{'pk:self.object.id'}})


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, 'home.html', {'task1': task1})


def details(request):
    task = Task.objects.all()
    return render(request, 'Details.html', {'task': task})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})
