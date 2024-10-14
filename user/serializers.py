from rest_framework import serializers
from .models import CustomUser, TechnicianProfile, PharmacyProfile


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "user_type"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data["email"], user_type=validated_data["user_type"]
        )
        user.set_password(validated_data["password"])  # Şifreyi hash'liyoruz
        user.save()
        return user


class TechnicianProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = TechnicianProfile
        fields = [
            "user",
            "name",
            "district",
            "birth_date",
            "phone_number",
            "national_id",
            "daily_job",
            "permanent_job",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = CustomUserSerializer.create(
            CustomUserSerializer(), validated_data=user_data
        )
        technician_profile = TechnicianProfile.objects.create(
            user=user, **validated_data
        )
        return technician_profile


class PharmacyProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = PharmacyProfile
        fields = [
            "user",
            "pharmacy_name",
            "responsible_person",
            "address",
            "gln_number",
            "daily_job",
            "permanent_job",
        ]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = CustomUserSerializer.create(
            CustomUserSerializer(), validated_data=user_data
        )
        pharmacy_profile = PharmacyProfile.objects.create(user=user, **validated_data)
        return pharmacy_profile
