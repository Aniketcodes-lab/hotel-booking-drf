from rest_framework import serializers
from django.utils import timezone
from math import ceil

from booking.models import Booking, Room
from booking.services.availability import get_available_rooms

class BookingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = [
            "id",
            "room",
            "booking_type",
            "start_time",
            "end_time",
            "total_price",
        ]
        read_only_fields = ["total_price"]
        
    def validate(self, data):
        start_time = data["start_time"]
        end_time = data["end_time"]

        if start_time >= end_time:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        if start_time < timezone.now():
            raise serializers.ValidationError(
                "Booking cannot start in the past."
            )

        return data
    
    def validate_room(self, room):
        start_time = self.initial_data.get("start_time")
        end_time = self.initial_data.get("end_time")

        if not start_time or not end_time:
            return room

        available_rooms = get_available_rooms(start_time, end_time)

        if room not in available_rooms:
            raise serializers.ValidationError(
                "Room is not available for the selected time."
            )

        return room
    
    def create(self, validated_data):
        request = self.context["request"]
        room = validated_data["room"]
        booking_type = validated_data["booking_type"]
        start_time = validated_data["start_time"]
        end_time = validated_data["end_time"]

        if booking_type == "hourly":
            hours = ceil(
                (end_time - start_time).total_seconds() / 3600
            )
            total_price = hours * room.hourly_price

        else:  # daily
            days = (end_time.date() - start_time.date()).days
            if days <= 0:
                days = 1
            total_price = days * room.daily_price

        booking = Booking.objects.create(
            user=request.user,
            total_price=total_price,
            **validated_data
        )

        return booking

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"