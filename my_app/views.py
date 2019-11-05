from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from . import models



# Create your views here.
def home(request):
    todo_items = models.ToDo.objects.all().order_by('-added_date')
    print(todo_items)
    return render(request,'my_app/index.html',{'todo_items': todo_items })

def add(request):
    content = request.POST['content']
    add_date = timezone.now()
    models.ToDo.objects.create(added_date = add_date, text = content)
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    models.ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")