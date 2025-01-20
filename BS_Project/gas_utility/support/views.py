from django.shortcuts import render
from customers.models import ServiceRequest
from django.contrib.auth.decorators import user_passes_test

# Ensure only support staff can access these views
@user_passes_test(lambda u: u.groups.filter(name='Support').exists())
def manage_requests(request):
    service_requests = ServiceRequest.objects.filter(status='Pending')
    return render(request, 'support/manage_requests.html', {'service_requests': service_requests})

@user_passes_test(lambda u: u.groups.filter(name='Support').exists())
def request_details(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'support/request_details.html', {'service_request': service_request})
