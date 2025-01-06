from django.contrib.admin import (
    ModelAdmin,
    # Methods
    register,
)

from apps.authority.models.class_model import Institute, StudyClass


@register(Institute)
class InstituteAdmin(ModelAdmin):
    """
    Admin interface for the Institute model.
    """

    list_display = (
        "id",
        "institute_name",
        "institute_address",
        "is_active",
    )
    list_editable = ("is_active",)
    list_display_links = ("id",)
    search_fields = (
        "id",
        "institute_name",
    )
    list_filter = ("is_active",)
    list_per_page = 50


@register(StudyClass)
class StudyClassAdmin(ModelAdmin):
    """
    Admin interface for the Institute model.
    """

    list_display = (
        "id",
        "class_name",
        "is_active",
    )
    list_editable = ("is_active",)
    list_display_links = ("id",)
    search_fields = (
        "id",
        "class_name",
    )
    list_filter = ("is_active",)
    list_per_page = 50
