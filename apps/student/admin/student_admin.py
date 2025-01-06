from django.contrib.admin import (
    ModelAdmin,
    # Methods
    register,
)

from apps.student.models.student_model import StudentProfile


@register(StudentProfile)
class StudentProfileAdmin(ModelAdmin):
    """
    Admin interface for the student profile model.
    """

    list_display = (
        "id",
        "student_user",
        "institute",
        "study_class",
        "guardian_name",
        "relation_with_guardian",
        "contact_number",
        "date_of_birth",
        "address",
        "profile_photo",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "student_user__username",
        "student_user__email",
        "student_user__name",
    )
    list_per_page = 50
