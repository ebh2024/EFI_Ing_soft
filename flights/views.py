from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Flight, Seat, Booking

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Flight, Seat, Booking

def flight_list(request):
    try:
        flights = Flight.objects.all()
        return render(request, 'flights/flight_list.html', {'flights': flights})
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})

def login_view(request):
    try:
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
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})

def logout_view(request):
    try:
        logout(request)
        return redirect('flight_list')
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})

def seat_availability(request, flight_id):
    try:
        flight = get_object_or_404(Flight, pk=flight_id)
        seats = Seat.objects.filter(flight=flight)
        return render(request, 'flights/seat_availability.html', {'flight': flight, 'seats': seats})
    except ObjectDoesNotExist:
        return render(request, 'flights/error.html', {'error_message': 'Flight not found'})
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})

def passengers_by_flight(request, flight_id):
    try:
        flight = get_object_or_404(Flight, pk=flight_id)
        bookings = Booking.objects.filter(flight=flight)
        passengers = [booking.passenger for booking in bookings]
        return render(request, 'flights/passengers_by_flight.html', {'flight': flight, 'passengers': passengers})
    except ObjectDoesNotExist:
        return render(request, 'flights/error.html', {'error_message': 'Flight not found'})
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})

def home(request):
    try:
        return render(request, 'flights/home.html')
    except Exception as e:
        return render(request, 'flights/error.html', {'error_message': str(e)})
