from django.contrib import admin
from .models import Flight, Passenger, Booking, Aircraft, Seat

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Booking)
admin.site.register(Aircraft)
admin.site.register(Seat)
