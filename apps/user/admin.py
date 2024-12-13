from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

from apps.user.models import User


@admin.register(User)
class UserAdmin(UA):
    ordering = ("-id",)
    # inlines = (EmailInline,)
    search_fields = ("email", "username")
    list_filter = ("is_active", "is_staff", "is_superuser", "user_type")
    list_display = (
        "id",
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "created_at",
        "updated_at",
        "user_type",
    )
    fieldsets = (
        (
            "Login Info",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_type",
                ),
            },
        ),
        (
            "Personal Info",
            {"classes": ("wide",), "fields": ("name", "email", "phone")},
        ),
        (
            "User Role",
            {
                "classes": ("collapse",),
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Timestamps",
            {"classes": ("collapse",), "fields": (("created_at", "updated_at"),)},
        ),
    )

    add_fieldsets = (
        (
            "Login Info",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_type",
                ),
            },
        ),
        (
            "Personal Info",
            {"classes": ("wide",), "fields": ("name", "email", "phone")},
        ),
        (
            "User Role",
            {
                "classes": ("collapse",),
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        # ('Important Dates', {
        #     'classes': ('collapse', ),
        #     'fields': (("created_at", "updated_at"),)
        # }),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
