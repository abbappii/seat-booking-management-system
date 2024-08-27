from django.db import models
from django.contrib.auth.models import User

from .choices import BookingChoices


class Venue(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200)
    total_seats = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    capacity = models.PositiveIntegerField()
    amenities = models.JSONField(
        default=dict, help_text="JSON format for amenities list."
    ) # using this for different amenities available at the venue.
    image = models.ImageField(upload_to="venues/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    venue = models.ForeignKey(Venue, related_name="events", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("venue", "name", "start_time")

    def __str__(self):
        return f"{self.name} at {self.venue.name}"


class SeatType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    price_multiplier = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)

    def __str__(self):
        return self.name


class Seat(models.Model):
    venue = models.ForeignKey(Venue, related_name="seats", on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name="event_seats", on_delete=models.CASCADE
    )
    seat_type = models.ForeignKey(
        SeatType, related_name="seats", on_delete=models.CASCADE
    )
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("venue", "event", "seat_number")

    def __str__(self):
        return f"{self.seat_number} ({self.seat_type.name}) at {self.venue.name}"




class Booking(models.Model):
    user = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, related_name="booking", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=BookingChoices.choices, default="PENDING")
    booking_time = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    payment_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.seat}"
