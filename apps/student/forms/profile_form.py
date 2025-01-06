from django.forms import ModelForm, ImageField, DateField, DateInput
from django.contrib.auth.forms import UserCreationForm

# models
from apps.student.models.student_model import StudentProfile


# Widgets
from common.widgets import CustomPictureImageFieldWidget


class StudentProfileForm(ModelForm):
    profile_photo = ImageField(required=False)
    date_of_birth = DateField(widget=DateInput(attrs={"type": "date"}))

    class Meta:
        model = StudentProfile
        exclude = ("student_user",)
