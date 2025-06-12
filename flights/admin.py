from django.contrib import admin
from .models import Flight, Passenger, Booking, Aircraft

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Booking)
admin.site.register(Aircraft)
