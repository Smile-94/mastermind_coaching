from django.http import JsonResponse

# class Based View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from apps.authority.models.course_model import EnrolledStudent, Batch
from apps.authority.forms.course_form import EnrolledStudentForm
from apps.student.models.student_model import StudentProfile
from apps.teacher.models.profile_model import TeacherProfile

# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# Filters
from apps.authority.filters.course_filter import BatchFilter
from apps.teacher.permission import TeacherPassesTestMixin


class TeacherCourseEnrollmentView(LoginRequiredMixin, TeacherPassesTestMixin, ListView):
    model = Batch
    queryset = Batch.objects.filter(is_active=True).order_by("-id")
    filterset_class = BatchFilter
    template_name = "teacher/enrolled_course.html"

    def get_context_data(self, **kwargs):
        try:
            teacher = TeacherProfile.objects.get(
                id=self.request.user.teacher_profile.id
            )
        except Exception as e:
            print(e)
        context = super().get_context_data(**kwargs)
        context["title"] = "Enrollment List"
        if teacher:
            context["batch_list"] = self.filterset_class(
                self.request.GET,
                queryset=self.queryset.filter(course_instructor=teacher),
            )
        return context
