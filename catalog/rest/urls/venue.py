from django.urls import path
from ..views import venue

urlpatterns = [
    path("", venue.VenueList.as_view(), name="venues-list-create"),
    path("<int:id>", venue.VenueDetail.as_view(), name="venue-detail"),
]
