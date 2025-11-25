
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from django.db.models import Q

from .models import Movie, Show, Booking
from .serializers import SignupSerializer, MovieSerializer, ShowSerializer, BookingSerializer


# ---------------- AUTH -------------------

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            return Response({"error": "Invalid credentials"}, status=400)

        if not user.check_password(password):
            return Response({"error": "Invalid credentials"}, status=400)

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })


# ---------------- MOVIES -------------------

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieShowListView(APIView):
    def get(self, request, id):
        shows = Show.objects.filter(movie_id=id)
        return Response(ShowSerializer(shows, many=True).data)


# ---------------- BOOKINGS -------------------

class BookSeatView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        seat_number = request.data.get("seat_number")

        try:
            show = Show.objects.get(id=id)
        except:
            return Response({"error": "Show not found"}, status=404)

        # Validate seat range
        if int(seat_number) < 1 or int(seat_number) > show.total_seats:
            return Response({"error": "Invalid seat number"}, status=400)

        # Prevent double booking
        if Booking.objects.filter(show=show, seat_number=seat_number, status="booked").exists():
            return Response({"error": "Seat already booked"}, status=400)

        booking = Booking.objects.create(
            user=request.user,
            show=show,
            seat_number=seat_number
        )

        return Response(BookingSerializer(booking).data, status=201)


class CancelBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        try:
            booking = Booking.objects.get(id=id, user=request.user)
        except:
            return Response({"error": "Booking not found"}, status=404)

        booking.status = "cancelled"
        booking.save()

        return Response({"message": "Booking cancelled"})


class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)