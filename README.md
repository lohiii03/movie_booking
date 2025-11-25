# 🎬 Movie Ticket Booking System (Django + DRF)

## 🚀 Features
- JWT Auth (Signup/Login)
- Movie & Show listing
- Seat booking with double-booking protection
- Booking cancellation
- Swagger API docs (/swagger/)

## ▶️ Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## 🔐 JWT
POST /login
→ returns access token

Add to Header:
Authorization: Bearer <token>