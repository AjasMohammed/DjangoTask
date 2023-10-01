from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserAuthForm, EventCreationForm
import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    user = request.user
    print(user.is_authenticated)
    if user.is_authenticated:
        base_url = 'http://127.0.0.1:8000/'
        if request.method == 'POST':
            form = EventCreationForm(request.POST)
            print(form)
            print(form.is_valid())
            if form.is_valid():
                data = {'title' : form.cleaned_data['title'],
                'time' : form.cleaned_data['time'],
                'date' : form.cleaned_data['date'],
                'description' : form.cleaned_data['description']}

                # response = requests.post(base_url+'post-event', data=data)
                # print(response.status_code)
        else:
            form = EventCreationForm()

        return render(request,'home/home.html', {'form': form})
    else:
        return redirect('auth/')

def auth(request):
    if request.method =='POST':
        form = UserAuthForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    else:
        form = UserAuthForm()
    return render(request, 'home/auth.html', {'form': form})