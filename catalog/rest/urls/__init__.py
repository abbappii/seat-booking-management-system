from django.urls import path, include

urlpatterns = [
    path("venues/", include("catalog.rest.urls.venue"))
]
