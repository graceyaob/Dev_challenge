from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required
def index(request):
    # return HttpResponse('hello world !')
    return render(request, 'home/index.html', {})

def signin(request):
    if request.user.is_authenticated: 
        return redirect('stations')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request = request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('stations')
    return render(request, 'home/sign-in.html', {})

def signup(request):
    if request.user.is_authenticated: 
        return redirect('stations')
    
    if request.method == 'POST':
        data = request.POST
        email, username, password = data.get("email"), data.get("username"), data.get("password")
        User.objects.create_user(username, email, password)
        user = authenticate(request = request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('stations')
        return redirect('home')

    context = {
        'form': None,
    }
    return render(request, 'home/sign-up.html', context)

def logout_view(request):
    logout(request)
    return redirect('signin')

def statistics(request):
    context = {}
    return render(request, 'home/statistics.html', context)

def forgot_password(request):
    context = {}
    return render(request, 'home/sign-in.html', context)

def stations(request):
    url = "https://airqino-api.magentalab.it/getStations/Arezzo"
    context = {
        'stations': requests.get(url).json()
    }
    print(stations)
    return render(request, 'home/stations.html', context)

@login_required
def station_check(request, station_name):
    url = "https://airqino-api.magentalab.it/getCurrentValues/" + station_name
    context = {
        'station': requests.get(url).json()
    }
    print(context['station'])
    return render(request, 'home/sensors.html', context)
    