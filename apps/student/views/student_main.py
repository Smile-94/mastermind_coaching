# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


# custom UserpassTestMixin
from apps.student.permission import StudentPassesTestMixin

# class Based View
from django.views.generic import TemplateView

# Models
from apps.user.models import User
from common.models import UserTypeChoice
from apps.authority.models.notice_model import (
    Notice,
    PublishedStatusChoice,
    NoticePublishedForChoice,
)
from apps.authority.models.course_model import Batch, EnrolledStudent, Assignment


# Create your views here.
class StudentHomeView(LoginRequiredMixin, StudentPassesTestMixin, TemplateView):
    template_name = "student/index.html"

    def get_context_data(self, **kwargs):
        student_profile = self.request.user.student_profile
        student = EnrolledStudent.objects.get(enrolled_student=student_profile)
        context = super().get_context_data(**kwargs)

        # Get the enrolled batches for the student
        enrolled_batches = EnrolledStudent.objects.filter(
            enrolled_student=student_profile
        ).values_list("enrolled_batch", flat=True)

        # Get assignments for the student's batches that are pending
        pending_assignments = Assignment.objects.filter(
            batch__in=enrolled_batches,  # Assignments for the student's batch
            due_date__gte=timezone.now(),  # Due date has not passed
        ).exclude(
            submitted_assignment__submitted_student=student  # Not yet submitted
        )

        context["title"] = "Student Panel"
        context["enrolled_batch"] = enrolled_batches.count()
        context["pending_assignment_count"] = pending_assignments.count()
        context["latest_notice"] = (
            Notice.objects.exclude(published_status=PublishedStatusChoice.ARCHIVED)
            .filter(
                published_for__in=[
                    NoticePublishedForChoice.STUDENT,
                    NoticePublishedForChoice.ALL,
                ]
            )
            .order_by("-id")[:10]
        )
        return context


class StudentProfileView(LoginRequiredMixin, StudentPassesTestMixin, TemplateView):
    template_name = "student/profile_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Profile Details"
        return context
