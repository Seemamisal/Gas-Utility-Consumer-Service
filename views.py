from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

# Submit Service Request
class ServiceRequestCreateView(generics.CreateAPIView):
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Track Service Requests
class ServiceRequestListView(generics.ListAPIView):
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)

# Update Service Request (For Admins/Support Team)
class ServiceRequestUpdateView(generics.UpdateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]
