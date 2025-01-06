from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.contrib import messages

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# Filters
from apps.authority.filters.course_filter import CourseFilter

# Generics Views
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Models
from apps.authority.models.course_model import Course

# Forms
from apps.authority.forms.course_form import CourseForm


class CourseInfoView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Course
    queryset = Course.objects.filter(is_active=True)
    form_class = CourseForm
    filterset_class = CourseFilter
    template_name = "authority/course/add_course.html"
    success_url = reverse_lazy("authority:course_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Week Days"
        context["courses"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context

    def form_valid(self, form):
        messages.success(self.request, "Course Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class CourseUpdateView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "authority/course/add_course.html"
    success_url = reverse_lazy("authority:course_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Courses"
        context["updated"] = True
        return context

    def form_valid(self, form):
        messages.success(self.request, "Course Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class DeleteCourseDaysView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model = Course
    context_object_name = "object"
    template_name = "authority/course/delete_course.html"
    success_url = reverse_lazy("authority:course_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Course"
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)
