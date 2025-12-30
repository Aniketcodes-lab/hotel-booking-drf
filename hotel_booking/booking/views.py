from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView
)

from booking.models import Booking
from booking.services.availability import get_available_rooms
from booking.serializers.room import RoomSerializer
from booking.serializers.booking import (
    BookingCreateSerializer,
    BookingListSerializer,
)
from booking.serializers.actions import (
    BookingCheckInSerializer,
    BookingCheckOutSerializer,
    BookingCancelSerializer,
)
from rest_framework import status

class AvailableRoomsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_time = parse_datetime(request.query_params.get("start_time"))
        end_time = parse_datetime(request.query_params.get("end_time"))

        if not start_time or not end_time:
            return Response(
                {"error": "Invalid or missing start_time/end_time"},
                status=400
            )

        rooms = get_available_rooms(start_time, end_time)
        return Response(RoomSerializer(rooms, many=True).data)

class BookingCreateView(CreateAPIView):
    serializer_class = BookingCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

class BookingListView(ListAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class BookingDetailView(RetrieveAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class BookingCheckInView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk, user=request.user)
        serializer = BookingCheckInSerializer(instance=booking)
        serializer.save()
        return Response({"status": booking.status})

class BookingCheckOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk, user=request.user)
        serializer = BookingCheckOutSerializer(instance=booking)
        serializer.save()
        return Response({"status": booking.status})

class BookingCancelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        booking = Booking.objects.get(pk=pk, user=request.user)

        # 🔐 HARD BLOCK – this is the key fix
        if booking.status != "BOOKED":
            return Response(
                {
                    "error": "Only bookings in BOOKED state can be cancelled."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        booking.status = "CANCELLED"
        booking.save()

        return Response(
            {"status": "CANCELLED"},
            status=status.HTTP_200_OK,
        )
