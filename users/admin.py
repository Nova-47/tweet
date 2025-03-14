from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("username", "password", "name", "email"),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "name",
    )
