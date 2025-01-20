from django.urls import path
from . import views

urlpatterns = [
    path('submit-request/', views.submit_service_request, name='submit_request'),
    path('request-status/', views.request_status, name='request_status'),
    path('account/', views.account_info, name='account_info'),
]
