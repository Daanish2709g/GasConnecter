from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path("create/", views.create_service_request, name="create_request"),
    path("track/", views.track_requests, name="track_requests"),
]
