from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...models import Booking
from ..serializers.booking import BookingSerializer

"""
API Views
    - Booking CRUD operation
"""

# applying permission for booking need a user, who is booking this ticket

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.filter()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.filter()
    serializer_class = BookingSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
