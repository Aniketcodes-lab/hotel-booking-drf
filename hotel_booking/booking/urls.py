from django.urls import path
from booking.views import (
    AvailableRoomsView,
    BookingCreateView,
    BookingListView,
    BookingDetailView,
    BookingCheckInView,
    BookingCheckOutView,
    BookingCancelView,
)

urlpatterns = [
    path("rooms/available/", AvailableRoomsView.as_view()),

    path("bookings/", BookingCreateView.as_view()),
    path("bookings/list/", BookingListView.as_view()),
    path("bookings/<int:pk>/", BookingDetailView.as_view()),

    path("bookings/<int:pk>/check-in/", BookingCheckInView.as_view()),
    path("bookings/<int:pk>/check-out/", BookingCheckOutView.as_view()),
    path("bookings/<int:pk>/cancel/", BookingCancelView.as_view()),
]
