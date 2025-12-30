from django.conf import settings
from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=20, unique=True)
    room_type = models.CharField(max_length=50)  # e.g. Deluxe, Suite
    hourly_price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

User = settings.AUTH_USER_MODEL

class Booking(models.Model):

    BOOKING_TYPE_CHOICES = (
        ("hourly", "Hourly"),
        ("daily", "Daily"),
    )

    STATUS_CHOICES = (
        ("BOOKED", "Booked"),
        ("CHECKED_IN", "Checked In"),
        ("CHECKED_OUT", "Checked Out"),
        ("CANCELLED", "Cancelled"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="bookings"
    )

    booking_type = models.CharField(
        max_length=10, choices=BOOKING_TYPE_CHOICES
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    total_price = models.DecimalField(
        max_digits=10, decimal_places=2
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="BOOKED"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - Room {self.room.room_number}"
