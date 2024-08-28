from ...models import SeatType, Seat, Event, Venue
from ..serializers.venue import VenueSerializer
from ..serializers.event import EventSerializer

from rest_framework import serializers


class SeatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatType
        fields = [
            "id",
            "name",
            "description",
            "base_price",
            "price_multiplier"
        ]


class SeatSerializer(serializers.ModelSerializer):
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source="venue",
        write_only=True,
    )
    venue = VenueSerializer(read_only=True)

    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source="event",
        write_only=True,
    )
    event = EventSerializer(read_only=True)

    seat_type_id = serializers.PrimaryKeyRelatedField(
        queryset=SeatType.objects.all(),
        source="seat_type",
        write_only=True,
    )
    seat_type = SeatTypeSerializer(read_only=True)

    class Meta:
        model = Seat
        fields = [
            "id",
            "venue_id",
            "venue",
            "event_id",
            "event",
            "seat_type_id",
            "seat_type",
            "seat_number",
            "is_available",
            "price",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["price"]
