from django.shortcuts import render, get_object_or_404, redirect
from apps.customers.models import ServiceRequest

def list_service_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, "support/request_list.html", {"requests": requests})

def update_request_status(request, pk):
    request_obj = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == "POST":
        request_obj.status = request.POST.get("status")
        request_obj.save()
        return redirect("support:request_list")
    return render(request, "support/request_details.html", {"request_obj": request_obj})
