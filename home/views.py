from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
from datetime import datetime
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
    return render(request, 'home/stations.html', context)

@login_required
def station_check(request, station_name):
    url = "https://airqino-api.magentalab.it/getCurrentValues/" + station_name
    context = {
        'station': requests.get(url).json()
    }
    return render(request, 'home/sensors.html', context)
    
def periode(request):

    url = "https://airqino-api.magentalab.it/getStations/Arezzo"
    stations = requests.get(url).json()

    feedback = None

    if request.method == 'POST':
        start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()
        station_name = request.POST['station_name']

        url = f"https://airqino-api.magentalab.it/{station_name}/{start_date}/{end_date}"
        print(url)

    context = {
        'stations': stations
    }
    return render(request, 'home/periode.html', context)