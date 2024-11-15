from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def create_service_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("customers:track_requests")
    else:
        form = ServiceRequestForm()
    return render(request, "customers/request_form.html", {"form": form})

def track_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, "customers/request_status.html", {"requests": requests})
