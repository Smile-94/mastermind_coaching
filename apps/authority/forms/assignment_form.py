from django.forms import ModelForm, DateTimeField, DateTimeInput

# models
from apps.authority.models.course_model import Assignment


class AssignmentForm(ModelForm):
    due_date = due_date = DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = Assignment
        fields = (
            "assignment_title",
            "description",
            "assignment_file",
            "due_date",
        )
