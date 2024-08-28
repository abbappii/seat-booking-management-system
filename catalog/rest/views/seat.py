from rest_framework import generics

from ...models import Seat, SeatType
from ..serializers.seat import SeatSerializer, SeatTypeSerializer

"""
API Views
    - Seat and SeatType CRUD operation
"""


class SeatList(generics.ListCreateAPIView):
    queryset = Seat.objects.filter()
    serializer_class = SeatSerializer


class SeatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.filter()
    serializer_class = SeatSerializer
    lookup_field = "id"


class SeatTypeList(generics.ListCreateAPIView):
    queryset = SeatType.objects.filter()
    serializer_class = SeatTypeSerializer


class SeatTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SeatType.objects.filter()
    serializer_class = SeatTypeSerializer
    lookup_field = "id"
