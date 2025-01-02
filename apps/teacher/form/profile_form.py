from django.forms import ModelForm, ImageField, DateField, DateInput
from django.contrib.auth.forms import UserCreationForm

# models
from apps.teacher.models.profile_model import (
    TeacherProfile,
    Address,
    EducationalQualification,
)


# Widgets
from common.widgets import CustomPictureImageFieldWidget


class TeacherProfileForm(ModelForm):
    profile_picture = ImageField()
    date_of_birth = DateField(widget=DateInput(attrs={"type": "date"}))

    class Meta:
        model = TeacherProfile
        exclude = ("profile_of",)
