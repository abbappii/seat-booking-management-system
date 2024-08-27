from rest_framework import generics

from ...models import Event
from ..serializers.event import EventSerializer

"""
API Views
    - Event CRUD operation
"""


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.filter()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.filter()
    serializer_class = EventSerializer
    lookup_field = "id"

