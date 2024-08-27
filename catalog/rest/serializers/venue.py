from rest_framework import serializers
from ...models import Venue


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = [
            "id",
            "name",
            "location",
            "total_seats",
            "description",
            "capacity",
            "amenities",
            "image",
            "created_at",
            "updated_at",
        ]
