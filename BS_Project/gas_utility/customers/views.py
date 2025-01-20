from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/submit_request.html', {'form': form})

@login_required
def request_status(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customers/request_status.html', {'service_requests': service_requests})

@login_required
def account_info(request):
    return render(request, 'customers/account_info.html')


