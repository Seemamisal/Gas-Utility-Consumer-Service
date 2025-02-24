
from django.urls import path
from .views import ServiceRequestCreateView, ServiceRequestListView, ServiceRequestUpdateView

urlpatterns = [
    path('submit/', ServiceRequestCreateView.as_view(), name='submit_request'),
    path('track/', ServiceRequestListView.as_view(), name='track_request'),
    path('update/<int:pk>/', ServiceRequestUpdateView.as_view(), name='update_request'),
]
