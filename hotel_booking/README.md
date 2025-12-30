# 🏨 Hotel Room Booking System (Hourly & Daily) – Django Rest Framework

## 📌 Project Overview

This project is a **Django Rest Framework (DRF) backend** for a hotel room booking system that allows users to book hotel rooms on an **hourly or daily basis**.

The system focuses on:
- Preventing overlapping bookings
- Accurate price calculation
- Managing booking lifecycle
- Enforcing time-based and status-based validations

This is a **backend-only implementation** with REST APIs.

---

## 🚀 Features

- Search available rooms for a given time range
- Create hourly or daily room bookings
- Prevent double bookings using overlap detection
- Check-in and check-out functionality
- Cancel bookings before check-in
- View booking details and booking history
- User-based access control

---

## 🧱 Tech Stack

- Python
- Django
- Django Rest Framework
- SQLite / PostgreSQL

---

## 📂 Core Models

### Room
- room_number
- room_type
- hourly_price
- daily_price
- is_active

### Booking
- user
- room
- booking_type (hourly / daily)
- start_time
- end_time
- total_price
- status (BOOKED, CHECKED_IN, CHECKED_OUT, CANCELLED)
- created_at

---

## 🔗 API Endpoints

### Search Available Rooms
GET /api/rooms/available/

### Create Booking
POST /api/bookings/

### List Booking History
GET /api/bookings/list/

### Booking Details
GET /api/bookings/{id}/

### Check-In
POST /api/bookings/{id}/check-in/

### Check-Out
POST /api/bookings/{id}/check-out/

### Cancel Booking
POST /api/bookings/{id}/cancel/

---

## 🔄 Booking Flow

BOOKED → CHECKED_IN → CHECKED_OUT  
   ↘ CANCELLED

---

## ▶️ Run Project

pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver
