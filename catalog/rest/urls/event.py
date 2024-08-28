from django.urls import path
from ..views import event

urlpatterns = [
    path("", event.EventList.as_view(), name="event-list-create"),
    path("<int:id>", event.EventDetail.as_view(), name="event-detail"),
]

