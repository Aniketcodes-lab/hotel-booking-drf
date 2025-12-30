# Hotel Room Booking System (DRF)

## Overview
This project is a Django Rest Framework backend for a hotel room booking system
supporting hourly and daily bookings with overlap prevention and booking lifecycle
management.

## Features
- Search available rooms by time range
- Hourly and daily bookings
- Prevent overlapping bookings
- Price calculation based on booking type
- Booking lifecycle: Booked, Checked-in, Checked-out, Cancelled
- Authentication-protected APIs

## Tech Stack
- Python
- Django
- Django Rest Framework
- SQLite (default)

## API Endpoints
- GET /api/rooms/available/
- POST /api/bookings/
- GET /api/bookings/
- GET /api/bookings/{id}/
- POST /api/bookings/{id}/cancel/
- POST /api/bookings/{id}/check-in/
- POST /api/bookings/{id}/check-out/

## How to Run
1. Create virtualenv
2. Install requirements
3. Run migrations
4. Create superuser
5. Run server

## Notes
- System prevents overlapping bookings
- Cancellation allowed only before check-in
