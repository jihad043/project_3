from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Todo

def singup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')

        try:
            my_user = User.objects.create_user(fnm, emailid, pwd)
            my_user.save()
            user_model = User.objects.get(username=fnm)
            new_profile = Todo.objects.create(user=user_model)  # id নয়, object
            new_profile.save()
            login(request, my_user)
            return redirect('/')  # home page
        except:
            invalid = 'User already exists'
            return render(request, 'singup.html', {'invalid': invalid})

    # GET request এর জন্য
    return render(request, 'singup.html')
