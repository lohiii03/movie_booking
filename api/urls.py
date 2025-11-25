
from django.urls import path
from .views import (
    SignupView, LoginView,
    MovieListView, MovieShowListView,
    BookSeatView, CancelBookingView,
    MyBookingsView
)

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),

    path('movies/', MovieListView.as_view()),
    path('movies/<int:id>/shows/', MovieShowListView.as_view()),

    path('shows/<int:id>/book/', BookSeatView.as_view()),
    path('bookings/<int:id>/cancel/', CancelBookingView.as_view()),

    path('my-bookings/', MyBookingsView.as_view()),
]
