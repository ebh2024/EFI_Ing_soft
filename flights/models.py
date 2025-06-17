from django.core.validators import MinValueValidator
from django.db import models

class Aircraft(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    rows = models.IntegerField(default=10)
    columns = models.IntegerField(default=6)
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
    estado = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'Scheduled'),
            ('on_time', 'On Time'),
            ('delayed', 'Delayed'),
            ('cancelled', 'Cancelled'),
            ('completed', 'Completed'),
        ],
        default='scheduled',
    )
    precio_base = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.flight_number} - {self.origin} to {self.destination}"


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    tipo_documento = models.CharField(max_length=50, default='DNI')

    def __str__(self):
        return self.name


class Seat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=True, blank=True)
    numero = models.CharField(max_length=10)
    fila = models.IntegerField(null=True, blank=True)
    columna = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=20, default='economy')
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'),
            ('reserved', 'Reserved'),
            ('occupied', 'Occupied'),
        ],
        default='available',
    )

    def __str__(self):
        return f"Seat {self.seat_number} on {self.flight.flight_number} ({self.status})"


class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    rol = models.CharField(max_length=50, default='employee')

    def __str__(self):
        return self.username

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    passenger = models.ForeignKey(Passenger, on_delete=models.PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('confirmed', 'Confirmed'),
            ('pending', 'Pending'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending',
    )
    booking_date = models.DateField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    codigo_reserva = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.passenger.name} on {self.flight.flight_number}, Seat {self.seat.seat_number}"


class Ticket(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.ticket_number} for {self.booking.passenger.name} on {self.booking.flight.flight_number}"


class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    rol = models.CharField(max_length=50, default='employee')

    def __str__(self):
        return self.username
