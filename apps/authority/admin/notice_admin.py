from django.contrib.admin import (
    ModelAdmin,
    # Methods
    register,
)

from apps.authority.models.notice_model import Notice


@register(Notice)
class NoticeAdmin(ModelAdmin):
    """
    Admin interface for the Notice model.
    """

    list_display = (
        "id",
        "title",
        "published_status",
        "published_for",
        "created_at",
    )
    list_editable = ("published_status", "published_for")
    list_display_links = ("id",)
    search_fields = (
        "id",
        "institute_name",
    )
    ordering = ("-id",)
    list_filter = ("published_status", "published_for")
    list_per_page = 50
