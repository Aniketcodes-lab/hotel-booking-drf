from booking.models import Room, Booking

def get_available_rooms(start_time, end_time):
    """
    Returns queryset of rooms that are NOT booked
    between start_time and end_time
    """

    # Find rooms with overlapping bookings
    overlapping_bookings = Booking.objects.filter(
        start_time__lt=end_time,
        end_time__gt=start_time,
        status__in=["BOOKED", "CHECKED_IN"]
    ).values_list("room_id", flat=True)

    # Exclude those rooms
    available_rooms = Room.objects.filter(
        is_active=True
    ).exclude(id__in=overlapping_bookings)

    return available_rooms
