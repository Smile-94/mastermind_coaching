from django.forms import ModelForm, DateField, DateInput, TimeField, TimeInput
from django.core.exceptions import ValidationError

# models
from apps.authority.models.course_model import Course, Batch, WeekDays


class WeekDaysForm(ModelForm):
    class Meta:
        model = WeekDays
        fields = "__all__"


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class BatchForm(ModelForm):
    start_date = DateField(widget=DateInput(attrs={"type": "date"}))
    end_date = DateField(widget=DateInput(attrs={"type": "date"}))
    start_time = TimeField(widget=TimeInput(attrs={"type": "time"}))
    end_time = TimeField(widget=TimeInput(attrs={"type": "time"}))

    class Meta:
        model = Batch
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        course_instructor = cleaned_data.get("course_instructor")
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        class_days = cleaned_data.get("class_days")
        class_per_week = cleaned_data.get("class_per_week")

        # Validate class_days does not exceed class_per_week
        if class_days and len(class_days) > class_per_week:
            raise ValidationError(
                f"The selected days cannot exceed the allowed classes per week ({class_per_week})."
            )

        # Check for overlapping batches for the same instructor
        overlapping_batches = (
            Batch.objects.filter(
                course_instructor=course_instructor,
                start_date__lte=end_date,
                end_date__gte=start_date,
            )
            .filter(
                class_days__in=class_days,
                start_time__lt=end_time,
                end_time__gt=start_time,
            )
            .distinct()
        )

        if overlapping_batches.exists():
            raise ValidationError(
                "The instructor already has a batch scheduled with conflict days or times."
            )

        return cleaned_data
