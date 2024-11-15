from django.urls import path
from . import views

app_name = "support"

urlpatterns = [
    path("requests/", views.list_service_requests, name="request_list"),
    path("requests/<int:pk>/update/", views.update_request_status, name="update_status"),
]
