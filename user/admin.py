from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PharmacyProfile, TechnicianProfile


class CustomUserAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ("email", "first_name", "last_name", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


# Register the CustomUser with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PharmacyProfile)
admin.site.register(TechnicianProfile)
