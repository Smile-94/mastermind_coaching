from django.contrib.admin import (
    ModelAdmin,
    # Methods
    register,
)


from apps.authority.models.course_model import (
    Course,
    Batch,
    WeekDays,
    EnrolledStudent,
    Assignment,
    SubmittedAssignment,
    Attendance,
)


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


@register(EnrolledStudent)
class EnrolledStudentAdmin(ModelAdmin):
    """
    Admin interface for the EnrolledStudent model.
    """

    list_display = (
        "id",
        "enrolled_batch",
        "enrolled_student",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "enrolled_batch__batch_name",
        "enrolled_student__student_user__username",
    )
    list_per_page = 50


@register(Assignment)
class AssignmentAdmin(ModelAdmin):
    """
    Admin interface for the Assignment model.
    """

    list_display = (
        "id",
        "assignment_title",
        "due_date",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "assignment_title",
    )
    list_per_page = 50


@register(SubmittedAssignment)
class SubmittedAssignmentAdmin(ModelAdmin):
    """
    Admin interface for the SubmittedAssignment model.
    """

    list_display = (
        "id",
        "assignment",
        "submitted_student",
        "is_graded",
        "grade",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "assignment__assignment_title",
    )
    list_per_page = 50


@register(Attendance)
class AttendanceAdmin(ModelAdmin):
    """
    Admin interface for the Attendance model.
    """

    list_display = (
        "id",
        "attendance_date",
        "student",
        "is_present",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "attendance_date",
    )
    list_per_page = 50
