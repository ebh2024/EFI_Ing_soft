from .models import Flight, Seat, Booking

def get_all_flights():
    return Flight.objects.all()

def get_flight_by_id(flight_id):
    return Flight.objects.get(pk=flight_id)

def get_seats_by_flight(flight):
    return Seat.objects.filter(flight=flight)

def get_bookings_by_flight(flight):
    return Booking.objects.filter(flight=flight)
