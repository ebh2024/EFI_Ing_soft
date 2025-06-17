from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from . import services

def flight_list(request):
    try:
        flights = services.get_all_flights()
        return render(request, 'flights/flight_list.html', {'flights': flights})
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})

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

def seat_availability(request, flight_id):
    try:
        flight = services.get_flight_by_id(flight_id)
        seats = services.get_seats_by_flight(flight)
        return render(request, 'flights/seat_availability.html', {'flight': flight, 'seats': seats})
    except ObjectDoesNotExist:
        return render(request, 'flights/error.html', {'error_message': 'Flight not found'})
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})

def passengers_by_flight(request, flight_id):
    try:
        flight = services.get_flight_by_id(flight_id)
        bookings = services.get_bookings_by_flight(flight)
        passengers = [booking.passenger for booking in bookings]
        return render(request, 'flights/passengers_by_flight.html', {'flight': flight, 'passengers': passengers})
    except ObjectDoesNotExist:
        return render(request, 'flights/error.html', {'error_message': 'Flight not found'})
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})

def home(request):
    return render(request, 'flights/home.html')
