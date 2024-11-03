from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ("pharmacy", "Pharmacy"),
        ("technician", "Technician"),
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("Bu e-posta adresiyle kayıtlı bir kullanıcı zaten mevcut."),
        },
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Add is_staff
    is_superuser = models.BooleanField(default=False)  # Add is_superuser
    user_type = models.CharField(
        max_length=20, choices=USER_TYPES, default="technician"
    )  # New field

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Pharmacy Profile Model (Updated)
class PharmacyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pharmacy_name = models.CharField(max_length=255)
    responsible_person = models.CharField(max_length=100)  # Sorumlu kişi adı soyadı
    address = models.TextField()
    gln_number = models.CharField(max_length=13, unique=True)  # GLN No
    daily_job = models.BooleanField(default=False)  # Günlük iş istiyorum
    permanent_job = models.BooleanField(default=False)  # Kalıcı iş istiyorum

    def __str__(self):
        return self.pharmacy_name


class TechnicianProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  # Ad ve soyadı tek bir alanda saklıyoruz
    district = models.CharField(max_length=100)  # İlçe
    birth_date = models.DateField(null=True, blank=True)  # Optional
    phone_number = models.CharField(max_length=15)
    national_id = models.CharField(
        max_length=11, unique=True, null=True, blank=True
    )  # TC Kimlik No opsiyonel
    daily_job = models.BooleanField(default=False)  # Günlük iş istiyorum
    permanent_job = models.BooleanField(default=False)  # Kalıcı iş istiyorum

    def __str__(self):
        return self.name
