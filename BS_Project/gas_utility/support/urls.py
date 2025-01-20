from django.urls import path
from . import views

urlpatterns = [
    path('manage-requests/', views.manage_requests, name='manage_requests'),
    path('request-details/<int:request_id>/', views.request_details, name='request_details'),
]
