from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, PharmacyProfile, TechnicianProfile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "pharmacy":
            PharmacyProfile.objects.create(user=instance)
        elif instance.user_type == "technician":
            TechnicianProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == "pharmacy":
        instance.pharmacyprofile.save()
    elif instance.user_type == "technician":
        instance.technicianprofile.save()
