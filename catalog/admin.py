from django.contrib import admin

# Register your models here.
from .models import Event, Venue, SeatType,Seat

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Seat)
admin.site.register(SeatType)
