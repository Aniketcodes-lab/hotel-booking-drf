from django.contrib import admin
from booking.models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_number", "room_type", "hourly_price", "daily_price", "is_active")
    list_filter = ("is_active", "room_type")
    search_fields = ("room_number",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "room", "user", "booking_type", "status", "start_time", "end_time")
    list_filter = ("status", "booking_type")