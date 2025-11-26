# 🎟️ Ticket Booking System – Backend Assignment (AlignTurtle)

This project is a backend-only implementation of a **Movie Ticket Booking System**, built as part of the AlignTurtle Backend Internship assignment.  

It demonstrates clean API design, database modeling, proper backend fundamentals, and problem-solving skills.

---

## 🚀 1. Project Summary

The system allows users to:

- View movies and show timings  
- View available seats for each show  
- Book one or more seats  
- Prevent double-booking (validation)  
- Cancel booking and free seats  
- Seed the database with sample movies, shows, and seats  

This project focuses **only on backend** and exposes a clean REST API.

---

## 🧠 2. Approach & Architecture

### ✔ **2.1 Data Modeling**

The system is designed using four key models:

- **Movie** – Basic movie information  
- **Show** – A scheduled screening of a movie  
- **Seat** – Individual seat for each show (A01, A02, …)  
- **Booking** – Represents a customer booking with multiple seats  

Relationships:

- Movie ↔ Show → *1 movie has many shows*  
- Show ↔ Seat → *Each show has its own seat map*  
- Booking ↔ Seat → *Many-to-many relationship*

This structure ensures:

- Isolation of seat maps between different shows  
- Ability to validate seat availability  
- Ability to expand easily (screen, theatre, payments etc.)


### ✔ **2.2 Booking Logic**

While booking:

1. Check if selected seats belong to the show  
2. Check if seats are already booked  
3. If valid, create the booking  
4. Mark seats as booked (atomic update)

This prevents **race conditions** and **double bookings**.

Cancellation:

- When a booking is cancelled, seats are automatically marked as available again.

---

### ✔ **2.3 API Design Principles**

- RESTful design  
- Separate endpoints for shows, seats, bookings  
- Idempotent GET routes  
- Validation in serializers/views  
- Error responses follow JSON standards  
- Modular project structure  

---

### ✔ **2.4 Seed Script Logic**

The project includes a seed script to populate:

- Sample movies  
- Sample shows  
- Seats for each show (like A01, A02…)  

Running the script resets and recreates test data to help reviewers test quickly.

---

## 🛠 3. Tech Stack

- **Python / Django / Django REST Framework**
- **SQLite / PostgreSQL** (SQLite for development)
- **REST API JSON responses**
- Optional: Postman collection for API testing

---

## 📂 4. Folder Structure

project-root/
│
├── booking_project/ # Django project settings
├── tickets/ # Main app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── management/
│ └── commands/
│ └── seed_data.py
│
├── requirements.txt
├── db.sqlite3
├── README.md
└── manage.py


## ⚙️ 5. Setup Instructions

### **Step 1: Clone the repository**

git clone <your-repository-url>
cd <project-folder>


### **Step 2: Create a virtual environment**

python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

### **Step 3: Install dependencies**
pip install -r requirements.txt



### **Step 4: Apply migrations**

python manage.py migrate

### **Step 5: Seed sample data (important)**

python manage.py seed_data


This will create sample movies, shows, and seats.

### **Step 6: Run server**

python manage.py runserver

## 📡 6. API Endpoints (Quick Overview)

### 🎬 **Movies**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/movies/` | List movies |

### 🕒 **Shows**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/shows/` | List shows |
| GET | `/api/shows/<id>/available_seats/` | List unbooked seats for the show |

### 🎟 **Booking**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/bookings/` | Create a booking |
| DELETE | `/api/bookings/<id>/` | Cancel a booking |

---

## 📘 7. Example Booking JSON (POST)

{
"show": 1,
"seats": [3, 4],
"customer_name": "Lakshmi",
"customer_email": "lakshmi@example.com"
}


## 🧪 8. Testing Flow (Reviewer Friendly)

The typical flow to test:

1. Run `seed_data`  
2. GET `/api/shows/`  
3. GET `/api/shows/<id>/available_seats/`  
4. POST `/api/bookings/`  
5. GET available seats again → seats should be marked booked  
6. DELETE `/api/bookings/<id>/`  
7. Seats become available again

This demonstrates correctness + validation + consistent state.

---

## 📝 9. Notes for Reviewers

- Code follows REST standards and Django best practices  
- Prevents race conditions and double-booking  
- Clean modular structure  
- Seed script included for faster testing  
- Easily extendable to payments, seat categories, multiple screens, etc.

---

## 🙌 10. Author

**<BODDI LAKSHMI LOHITHA>**  
Backend Developer — AlignTurtle Assignment  
GitHub: *<lohiii03>*  
