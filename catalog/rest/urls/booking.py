from django.urls import path
from ..views import booking

urlpatterns = [
    path("", booking.BookingList.as_view(), name="booking-list-create"),
    path("<int:id>", booking.BookingDetail.as_view(), name="booking-detail"),
]
