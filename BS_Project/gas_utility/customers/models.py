from django.db import models
from django.contrib.auth.models import User

# Service Request Types
SERVICE_REQUEST_CHOICES = [
    ('installation', 'Installation'),
    ('maintenance', 'Maintenance'),
    ('emergency', 'Emergency'),
]

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=SERVICE_REQUEST_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='requests/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} - {self.customer.username} - {self.status}"
