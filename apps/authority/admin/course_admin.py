from django.contrib.admin import (
    ModelAdmin,
    # Methods
    register,
)


from apps.authority.models.course_model import Course, Batch, WeekDays


@register(WeekDays)
class WeekDaysAdmin(ModelAdmin):
    """
    Admin interface for the WeekDays model.
    """

    list_display = (
        "id",
        "days",
        "is_holiday",
        "is_active",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "days",
    )
    list_filter = ("is_holiday", "is_active")
    list_per_page = 50


@register(Course)
class CourseAdmin(ModelAdmin):
    """
    Admin interface for the Course model.
    """

    list_display = (
        "id",
        "course_name",
        "course_code",
        "course_fee",
    )

    list_display_links = ("id",)
    search_fields = (
        "id",
        "course_name",
        "course_code",
    )
    list_per_page = 50


@register(Batch)
class BatchAdmin(ModelAdmin):
    """
    Admin interface for the Batch model.
    """

    list_display = (
        "id",
        "batch_name",
        "start_date",
        "end_date",
        "student_class",
        "course",
        "course_instructor",
        "maximum_students",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "batch_name",
    )
    list_per_page = 50
