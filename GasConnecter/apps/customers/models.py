from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]
    customer_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to="attachments/", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service_type}"
