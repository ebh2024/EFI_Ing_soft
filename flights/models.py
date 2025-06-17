from django.db import models

class Aircraft(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    seat_layout = models.JSONField(null=True, blank=True)
    technical_information = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField(null=True, blank=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.flight_number} - {self.origin} to {self.destination}"


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'),
            ('reserved', 'Reserved'),
            ('occupied', 'Occupied'),
        ],
        default='available',
    )
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"Seat {self.seat_number} on {self.flight.flight_number} ({self.status})"


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    passenger = models.ForeignKey(Passenger, on_delete=models.PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.passenger.name} on {self.flight.flight_number}, Seat {self.seat.seat_number}"
