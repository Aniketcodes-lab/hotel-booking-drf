from rest_framework import serializers
from django.utils import timezone
from booking.models import Booking

class BookingCheckInSerializer(serializers.Serializer):

    def validate(self, attrs):
        booking = self.instance

        if booking.status != "BOOKED":
            raise serializers.ValidationError(
                "Only booked reservations can be checked in."
            )

        if timezone.now() < booking.start_time:
            raise serializers.ValidationError(
                "Cannot check in before booking start time."
            )

        return attrs

    def save(self):
        booking = self.instance
        booking.status = "CHECKED_IN"
        booking.save()
        return booking

class BookingCheckOutSerializer(serializers.Serializer):

    def validate(self, attrs):
        booking = self.instance

        if booking.status != "CHECKED_IN":
            raise serializers.ValidationError(
                "Only checked-in bookings can be checked out."
            )

        return attrs

    def save(self):
        booking = self.instance
        booking.status = "CHECKED_OUT"
        booking.save()
        return booking

class BookingCancelSerializer(serializers.Serializer):

    def validate(self, attrs):
        booking = self.instance

        if booking.status != "BOOKED":
            raise serializers.ValidationError(
                "Only booked reservations can be cancelled."
            )

        return attrs

    def save(self):
        booking = self.instance
        booking.status = "CANCELLED"
        booking.save()
        return booking
