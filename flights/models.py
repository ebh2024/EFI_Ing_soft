from django.db import models

class Aircraft(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.flight_number} - {self.origin} to {self.destination}"


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.passenger.name} on {self.flight.flight_number}"
