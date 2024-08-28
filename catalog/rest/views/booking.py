from rest_framework import generics

from ...models import Booking
from ..serializers.booking import BookingSerializer

"""
API Views
    - Booking CRUD operation
"""


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.filter()
    serializer_class = BookingSerializer


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.filter()
    serializer_class = BookingSerializer
    lookup_field = "id"
