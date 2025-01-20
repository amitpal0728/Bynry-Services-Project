from django import forms
from customers.models import ServiceRequest

class RequestStatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status', 'assigned_to']
