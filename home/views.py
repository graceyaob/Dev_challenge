from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    # return HttpResponse('hello world !')
    return render(request, 'home/index.html', {})

def signin(request):
    return render(request, 'home/sign-in.html', {})

def signup(request):
    userForm = UserCreationForm()

    if request.method == 'POST':
        userForm = UserCreationForm(request)
        if userForm.is_valid():
            userForm.save()
    context = {
        'form': userForm,
    }
    return render(request, 'home/sign-up.html', context)

def statistics(request):
    context = {}
    return render(request, 'home/statistics.html', context)

def forgot_password(request):
    context = {}
    return render(request, 'home/sign-in.html', context)