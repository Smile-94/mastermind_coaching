# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# class Based View
from django.views.generic import TemplateView

# Models


# Create your views here.
class AdminHomeView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):
    template_name = "authority/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel"
        return context
