# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# class Based View
from django.views.generic import TemplateView

# Models
from apps.user.models import User
from common.models import UserTypeChoice
from apps.authority.models.notice_model import Notice, PublishedStatusChoice


# Create your views here.
class AdminHomeView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):
    template_name = "authority/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel"
        context["total_student"] = User.objects.filter(
            user_type=UserTypeChoice.STUDENT, is_active=True
        ).count()
        context["total_teacher"] = User.objects.filter(
            user_type=UserTypeChoice.TEACHER, is_active=True
        ).count()
        context["latest_students"] = User.objects.filter(
            user_type=UserTypeChoice.TEACHER, is_active=True
        ).order_by("-id")[:10]
        context["latest_notice"] = Notice.objects.exclude(
            published_status=PublishedStatusChoice.ARCHIVED
        ).order_by("-id")[:10]
        return context
