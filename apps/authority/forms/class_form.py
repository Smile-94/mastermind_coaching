from django.forms import ModelForm

# models
from apps.authority.models.class_model import StudyClass, Institute


class StudyClassForm(ModelForm):
    class Meta:
        model = StudyClass
        exclude = ("is_active",)


class InstituteForm(ModelForm):
    class Meta:
        model = Institute
        exclude = ("is_active",)
