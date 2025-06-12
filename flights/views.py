from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Flight

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('flight_list')
        else:
            return render(request, 'flights/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'flights/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('flight_list')
