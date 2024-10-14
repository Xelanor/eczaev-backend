from rest_framework import generics
from .models import TechnicianProfile, PharmacyProfile
from .serializers import TechnicianProfileSerializer, PharmacyProfileSerializer


# API View for Technician Registration
class TechnicianRegisterView(generics.CreateAPIView):
    queryset = TechnicianProfile.objects.all()
    serializer_class = TechnicianProfileSerializer


# API View for Pharmacy Registration
class PharmacyRegisterView(generics.CreateAPIView):
    queryset = PharmacyProfile.objects.all()
    serializer_class = PharmacyProfileSerializer
