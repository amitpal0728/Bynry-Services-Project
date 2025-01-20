from customers.models import ServiceRequest
from django.db import models

class SupportRequest(ServiceRequest):
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=10, default='Normal')

    def __str__(self):
        return f"Support Request {self.id} - {self.status}"
