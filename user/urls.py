from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import TechnicianRegisterView, PharmacyRegisterView


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "register/technician/",
        TechnicianRegisterView.as_view(),
        name="technician-register",
    ),
    path(
        "register/pharmacy/",
        PharmacyRegisterView.as_view(),
        name="pharmacy-register",
    ),
]
