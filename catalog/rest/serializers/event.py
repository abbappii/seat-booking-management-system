from rest_framework import serializers

from ...models import Event, Venue
from ..serializers.venue import VenueSerializer

class EventSerializer(serializers.ModelSerializer):
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source="venue",
        write_only=True,
    )
    venue = VenueSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "venue_id",
            "venue",
            "name",
            "description",
            "start_time",
            "end_time",
            "is_active",
            "created_at",
            "updated_at"
        ]
