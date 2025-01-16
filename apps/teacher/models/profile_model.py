from django.utils.translation import gettext_lazy as _

# Django Model Fields
from django.db.models import (
    CharField,
    TextField,
    ImageField,
    ForeignKey,
    OneToOneField,
    DateField,
    PositiveBigIntegerField,
    # Functions
    CASCADE,
    TextChoices,
)

from common.models import DjangoBaseModel

# Import Relation Model
from apps.user.models import User


class MaritalStatusChoices(TextChoices):
    SINGLE = "single", "Single"
    MARRIED = "married", "Married"
    DIVORCED = "divorced", "Divorced"


class GenderChoices(TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"


class TeacherProfile(DjangoBaseModel):
    """
    Teacher Profile Model
    """

    profile_of = OneToOneField(
        User, related_name="teacher_profile", on_delete=CASCADE, unique=True
    )
    date_of_birth = DateField(null=True, blank=True)
    gender = CharField(
        max_length=10,
        choices=GenderChoices.choices,
        null=True,
        blank=True,
    )
    nationality = CharField(max_length=100, null=True, blank=True)
    nid_no = CharField(max_length=100, blank=True, null=True, unique=True)
    profile_picture = ImageField(upload_to="teacher_profiles/", null=True, blank=True)
    marital_status = CharField(
        max_length=15,
        choices=MaritalStatusChoices.choices,
        default=MaritalStatusChoices.SINGLE,
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.profile_of.name:
            return f"{self.profile_of.name}"
        else:
            return f"{self.profile_of.username}"


class Address(DjangoBaseModel):
    """
    Address Model
    """

    address_of = OneToOneField(User, on_delete=CASCADE, related_name="teacher_address")
    address = CharField(max_length=250, null=True, blank=True)
    city = CharField(max_length=100, null=True, blank=True)
    state = CharField(max_length=100, null=True, blank=True)
    country = CharField(max_length=100, null=True, blank=True)
    zip_code = CharField(max_length=20, null=True, blank=True)

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        app_label = "teacher"
        verbose_name = _("Address")
        verbose_name_plural = _("Address")

    def __str__(self):
        if self.profile_of.name:
            return f"{self.profile_of.name}'s address"
        else:
            return f"{self.profile_of.username}'s address"


class EducationalQualification(DjangoBaseModel):
    teacher = OneToOneField(User, on_delete=CASCADE, related_name="qualifications")
    degree = CharField(max_length=200)  # e.g., B.Ed., M.Ed., Ph.D.
    institution = CharField(max_length=255)  # Name of the university or institution
    passing_year = PositiveBigIntegerField(default=2024)
    grade_or_cgpa = CharField(max_length=20, null=True, blank=True)  # e.g., "A+", "4.0"
    specialization = CharField(max_length=200, null=True, blank=True)  # Optional field
    achievements = TextField(null=True, blank=True)  # Notable achievements or honors

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        app_label = "teacher"
        verbose_name = _("Educational Qualification")
        verbose_name_plural = _("Educational Qualification")

    def __str__(self):
        if self.teacher.name:
            return f"{self.teacher.name} {self.degree}'s"
        else:
            return f"{self.teacher.username} {self.degree}'s"
