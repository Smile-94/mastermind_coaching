from datetime import date

# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.teacher.permission import TeacherPassesTestMixin

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
from apps.authority.models.course_model import Batch, Attendance


# Create your views here.
class TeacherHomeView(LoginRequiredMixin, TeacherPassesTestMixin, TemplateView):
    template_name = "teacher/index.html"

    def get_context_data(self, **kwargs):
        teacher_profile = self.request.user.teacher_profile
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel"
        context["total_student"] = User.objects.filter(
            user_type=UserTypeChoice.STUDENT, is_active=True
        ).count()
        context["total_course"] = Batch.objects.filter(
            course_instructor=teacher_profile, is_active=True
        ).count()
        context["total_present"] = Attendance.objects.filter(
            batch__course_instructor=teacher_profile, attendance_date=date.today()
        ).count()
        context["latest_notice"] = Notice.objects.exclude(
            published_status=PublishedStatusChoice.ARCHIVED
        ).filter(
            published_for__in=[
                NoticePublishedForChoice.TEACHER,
                NoticePublishedForChoice.ALL,
            ]
        )
        return context


class TeacherProfileView(LoginRequiredMixin, TeacherPassesTestMixin, TemplateView):
    template_name = "teacher/profile_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel"
        return context
