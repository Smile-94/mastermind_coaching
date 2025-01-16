from django.shortcuts import render
from django.views.generic import ListView
from apps.authority.models.course_model import Batch
from collections import defaultdict

# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.teacher.permission import TeacherPassesTestMixin


class TeacherRoutineView(LoginRequiredMixin, TeacherPassesTestMixin, ListView):
    model = Batch
    template_name = "teacher/routine.html"
    context_object_name = "batches_by_day"

    def get_queryset(self):
        teacher_profile = (
            self.request.user.teacher_profile
        )  # Assuming a profile linked to user
        batches = Batch.objects.filter(course_instructor=teacher_profile).order_by(
            "start_date"
        )

        # Grouping batches by the days of the week
        batches_by_day = defaultdict(list)
        for batch in batches:
            for day in batch.class_days.all():
                batches_by_day[day.days].append(batch)
        return dict(batches_by_day)
