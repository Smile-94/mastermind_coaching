from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin


# custom UserpassTestMixin
from apps.teacher.permission import TeacherPassesTestMixin

# class Based View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Models
from apps.authority.models.course_model import Assignment, Batch, SubmittedAssignment


# forms
from apps.authority.forms.assignment_form import AssignmentForm
from apps.authority.forms.course_form import SubmittedAssignmentForm
from apps.authority.models.course_model import EnrolledStudent

# Filters
from apps.authority.filters.course_filter import EnrolledStudentFilter


class TeacherEnrolledStudentListView(
    LoginRequiredMixin, TeacherPassesTestMixin, ListView
):
    model = EnrolledStudent
    queryset = EnrolledStudent.objects.all()
    filterset_class = EnrolledStudentFilter
    template_name = "teacher/enrolled_student.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        context["title"] = "Student List"
        context["objects"] = self.filterset_class(
            self.request.GET,
            queryset=self.queryset.filter(
                enrolled_batch__course_instructor=self.request.user.teacher_profile,
                enrolled_batch__id=pk,
            ),
        )
        return context
