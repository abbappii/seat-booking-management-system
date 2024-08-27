from rest_framework import generics

from ...models import Venue
from ..serializers.venue import VenueSerializer

"""
API Views
    - Venue CRUD operation
"""

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.filter()
    serializer_class = VenueSerializer


class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.filter()
    serializer_class = VenueSerializer
    lookup_field = "id"

