from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

from apps.user.models import User, AdminProfile


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


# * <<------------------------------------*** Admin Profile Admin ***----------------------------->>
@admin.register(AdminProfile)
class EducationalQualificationAdmin(admin.ModelAdmin):
    """
    Admin interface for teacher educational qualification.
    """

    list_display = (
        "id",
        "user",
        "profile_picture",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "user__username",
        "user__email",
        "user__name",
    )
    list_per_page = 50
