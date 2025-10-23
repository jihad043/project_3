from django.shortcuts import render,redirect
from django.views import View
from .models import Todo
from .form import  TodoForm

from django.contrib import messages

def home (request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TodoForm()
    return render(request,'home.html',{'form':form})
        
        
        
def list (request):
    return render(request,'add_items.html')        