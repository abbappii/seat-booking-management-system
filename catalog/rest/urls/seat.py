from django.urls import path
from ..views import seat

urlpatterns = [
    path("", seat.SeatList.as_view(), name="seats-list-create"),
    path("<int:id>", seat.SeatDetail.as_view(), name="seat-detail"),
    path("type/", seat.SeatTypeList.as_view(), name="seat-type-list-create"),
    path("type/<int:id>", seat.SeatTypeDetail.as_view(), name="seat-type-list-create"),
]
