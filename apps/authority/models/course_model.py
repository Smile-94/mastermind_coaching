from django.db.models import (
    CharField,
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
)
from django.utils.translation import gettext_lazy as _
from common.models import DjangoBaseModel
from apps.teacher.models.profile_model import TeacherProfile
from apps.authority.models.class_model import StudyClass


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
