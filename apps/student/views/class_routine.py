from django.shortcuts import render
from django.views.generic import ListView
from apps.authority.models.course_model import Batch, EnrolledStudent
from collections import defaultdict

# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.student.permission import StudentPassesTestMixin


class StudentRoutineView(LoginRequiredMixin, StudentPassesTestMixin, ListView):
    model = Batch
    template_name = "student/routine.html"
    context_object_name = "batches_by_day"

    def get_queryset(self):
        student_profile = (
            self.request.user.student_profile
        )  # Assuming a profile linked to user
        # Filter batches through the EnrolledStudent model
        enrolled_batches = EnrolledStudent.objects.filter(
            enrolled_student=student_profile
        ).values_list("enrolled_batch", flat=True)
        # Query the Batch model for those specific batches
        batches = Batch.objects.filter(id__in=enrolled_batches).order_by("start_date")

        # Grouping batches by the days of the week
        batches_by_day = defaultdict(list)
        for batch in batches:
            for day in batch.class_days.all():
                batches_by_day[day.days].append(batch)
        return dict(batches_by_day)
