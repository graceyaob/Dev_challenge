from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
import requests

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

def stations(request):
    url = "https://airqino-api.magentalab.it/getStations/Arezzo"
    context = {
        'stations': requests.get(url).json()
    }
    print(stations)
    return render(request, 'home/stations.html', context)

def station_check(request, station_name):
    url = "https://airqino-api.magentalab.it/getCurrentValues/" + station_name
    context = {
        'station': requests.get(url).json()
    }
    print(context['station'])
    return render(request, 'home/sensors.html', context)
    