from django.urls import path, include

urlpatterns = [
    path("venues/", include("catalog.rest.urls.venue")),
    path("events/", include("catalog.rest.urls.event")),
    path("seats/", include("catalog.rest.urls.seat")),
    path("bookings/", include("catalog.rest.urls.booking")),
]
