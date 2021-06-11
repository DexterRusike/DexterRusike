from django.shortcuts import render
from django.utils import timezone
from . import models
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = models.Todo.objects.all().order_by('-added_date')
    return render(request, 'basic_app/index.html', {
    'todo_items': todo_items
    })

def add_todo(request):
    current_date = timezone.now()
    content = request.POST.get('content')
    models.Todo.objects.create(added_date=current_date,text=content)
    return HttpResponseRedirect('/')

def delete_todo(request, todo_id):
    models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
