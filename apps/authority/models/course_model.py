from django.db.models import (
    CharField,
    TextField,
    DecimalField,
    ForeignKey,
    CASCADE,
    DateField,
    PositiveIntegerField,
    TextChoices,
    BooleanField,
    SET_NULL,
    ManyToManyField,
    TimeField,
    FileField,
    DateTimeField,
)
from django.utils.translation import gettext_lazy as _
from common.models import DjangoBaseModel
from apps.teacher.models.profile_model import TeacherProfile
from apps.authority.models.class_model import StudyClass
from apps.student.models.student_model import StudentProfile


class WeekDaysChoices(TextChoices):
    FRIDAY = "friday", "Friday"
    SATURDAY = "saturday", "Saturday"
    SUNDAY = "sunday", "Sunday"
    MONDAY = "monday", "Monday"
    TUESDAY = "tuesday", "Tuesday"
    WEDNESDAY = "wednesday", "Wednesday"
    THURSDAY = "thursday", "Thursday"


class WeekDays(DjangoBaseModel):
    days = CharField(
        max_length=10, choices=WeekDaysChoices.choices, default=WeekDaysChoices.FRIDAY
    )
    is_holiday = BooleanField(default=False, blank=True, null=True)
    is_active = BooleanField(default=True, blank=True, null=True)

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        verbose_name = _("Week Days")

    def __str__(self):
        return self.days


class Course(DjangoBaseModel):
    course_name = CharField(max_length=255, unique=True)
    course_code = CharField(max_length=10, unique=True)
    course_fee = DecimalField(
        max_digits=20,
        decimal_places=4,
        default=0.0000,
        blank=True,
        null=True,
    )  # Course fee
    is_active = BooleanField(default=True, blank=True, null=True)  # Course status

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        verbose_name = _("Course")

    def __str__(self):
        return f"{self.course_name}-({self.course_code})"


class Batch(DjangoBaseModel):
    batch_name = CharField(max_length=255)
    start_date = DateField()
    end_date = DateField()
    student_class = ForeignKey(
        StudyClass, related_name="course_class", on_delete=CASCADE
    )
    course = ForeignKey(Course, related_name="batch_course", on_delete=CASCADE)
    course_instructor = ForeignKey(
        TeacherProfile, related_name="course_instructor", on_delete=CASCADE
    )
    maximum_students = PositiveIntegerField(default=1)
    class_per_week = PositiveIntegerField(default=1)
    start_time = TimeField(blank=True, null=True)
    end_time = TimeField(blank=True, null=True)
    class_days = ManyToManyField(WeekDays, related_name="batch_weekdays", blank=True)
    is_active = BooleanField(default=True, blank=True, null=True)

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        verbose_name = _("Batch")
        verbose_name_plural = _("Batch")

    def __str__(self):
        return self.batch_name


class EnrolledStudent(DjangoBaseModel):
    enrolled_batch = ForeignKey(Batch, related_name="enrolled_batch", on_delete=CASCADE)
    enrolled_student = ForeignKey(
        StudentProfile,
        related_name="batch_enrolled_student",
        on_delete=SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.enrolled_batch}-({self.enrolled_student.student_user.name})"


class Assignment(DjangoBaseModel):
    batch = ForeignKey(Batch, related_name="assignments_batch", on_delete=CASCADE)
    assignment_title = CharField(max_length=255)
    description = TextField(blank=True, null=True)
    assignment_file = FileField(upload_to="assignment/", blank=True, null=True)
    due_date = DateTimeField(blank=True, null=True)

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        verbose_name = _("Assignment")
        verbose_name_plural = _("Assignment")

    def __str__(self):
        return f"{self.batch}- {self.assignment_title}"


class SubmittedAssignment(DjangoBaseModel):
    assignment = ForeignKey(
        Assignment, related_name="submitted_assignment", on_delete=CASCADE
    )
    submitted_student = ForeignKey(
        EnrolledStudent,
        related_name="submitted_assignment",
        on_delete=CASCADE,
    )
    upload_file = FileField(upload_to="assignment/", blank=True, null=True)
    review_file = FileField(upload_to="assignment/", blank=True, null=True)
    is_graded = BooleanField(default=False, blank=True, null=True)
    grade = CharField(max_length=10, blank=True, null=True)
    description = TextField(blank=True, null=True)

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        verbose_name = _("Submitted Assignment")
        verbose_name_plural = _("Submitted Assignment")

    def __str__(self):
        return f"{self.assignment}-({self.submitted_student.enrolled_batch.batch_name})"


class Attendance(DjangoBaseModel):
    batch = ForeignKey(Batch, related_name="attendance_batch", on_delete=CASCADE)
    student = ForeignKey(
        StudentProfile, related_name="attendance_student", on_delete=CASCADE
    )
    attendance_date = DateField()
    is_present = BooleanField(default=True)  # True for Present, False for Absent

    class Meta:
        unique_together = (
            "batch",
            "student",
            "attendance_date",
        )  # Prevent duplicate entries
        verbose_name = _("Attendance")
        verbose_name_plural = _("Attendance")

    def __str__(self):
        status = "Present" if self.is_present else "Absent"
        return f"{self.student.student_user.name} - {self.batch.batch_name} ({status})"
