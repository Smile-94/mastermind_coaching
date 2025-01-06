from django.db.models import (
    CharField,
    DateField,
    OneToOneField,
    TextChoices,
    CASCADE,
    ImageField,
    ForeignKey,
)
from django.utils.translation import gettext_lazy as _
from common.models import DjangoBaseModel
from phonenumber_field.modelfields import PhoneNumberField
from apps.user.models import User
from apps.authority.models.class_model import Institute, StudyClass


class GenderChoices(TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"


class StudentProfile(DjangoBaseModel):
    student_user = OneToOneField(
        User, on_delete=CASCADE, related_name="student_profile"
    )
    institute = ForeignKey(
        Institute,
        on_delete=CASCADE,
        related_name="study_institute",
        blank=True,
        null=True,
    )
    study_class = ForeignKey(
        StudyClass,
        on_delete=CASCADE,
        related_name="students_class",
        blank=True,
        null=True,
    )
    guardian_name = CharField(max_length=150, blank=True, null=True)
    relation_with_guardian = CharField(max_length=150, blank=True, null=True)
    contact_number = PhoneNumberField(
        verbose_name=_("Contact Number"),
        unique=True,
        blank=True,
        null=True,
    )
    gender = CharField(
        max_length=10,
        choices=GenderChoices.choices,
        null=True,
        blank=True,
    )
    date_of_birth = DateField(blank=True, null=True)
    address = CharField(max_length=250, blank=True, null=True)
    profile_photo = ImageField(upload_to="students/", blank=True, null=True)

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        verbose_name = _("Student Profile")

    def __str__(self):
        return f"{self.student_user.name}'s profile"
