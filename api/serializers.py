from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Show, Booking


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ShowSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Show
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    show = ShowSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"