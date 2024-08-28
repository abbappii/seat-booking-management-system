from django.db import transaction

from rest_framework import serializers
from ...models import Booking, Seat

from ..serializers.seat import SeatSerializer


class BookingSerializer(serializers.ModelSerializer):
    seat = SeatSerializer(read_only=True)
    seat_id = serializers.PrimaryKeyRelatedField(
        queryset=Seat.objects.all(), source="seat", write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            "id",
            "user",
            "seat_id",
            "seat",
            "booking_time",
            "payment_status",
            "payment_amount",
            "payment_method",
            "transaction_id",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("user",)

    def validate(self, data):
        if self.instance and self.instance.seat == data.get("seat"):
            return data

        if not data["seat"].is_available:
            raise serializers.ValidationError(
                "This seat is already booked and not available for booking."
            )
        return data

    def create(self, validated_data):
        user = self.context["request"].user
        seat = validated_data["seat"]

        with transaction.atomic():
            seat = Seat.objects.select_for_update().get(pk=seat.pk)
            if not seat.is_available:
                raise serializers.ValidationError("This seat is already booked.")
            seat.is_available = False
            seat.save()

        validated_data["user"] = user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        new_seat = validated_data.get("seat", instance.seat)
        if new_seat != instance.seat:
            if not new_seat.is_available:
                raise serializers.ValidationError(
                    "The new seat is already booked and not available for booking."
                )

            new_seat.is_available = False
            new_seat.save()

            instance.seat.is_available = True # make the previous booking seat available for others
            instance.seat.save()

        return super().update(instance, validated_data)
