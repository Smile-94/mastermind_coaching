from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.contrib import messages

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# Filters
from apps.authority.filters.study_class_filter import StudyClassFilter

# Generics Views
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Models
from apps.authority.models.class_model import StudyClass

# Forms
from apps.authority.forms.class_form import StudyClassForm


class StudyClassInfoView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = StudyClass
    queryset = StudyClass.objects.filter(is_active=True)
    form_class = StudyClassForm
    filterset_class = StudyClassFilter
    template_name = "authority/add_class.html"
    success_url = reverse_lazy("authority:class_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Class"
        context["student_class"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context

    def form_valid(self, form):
        messages.success(self.request, "Class Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class StudyClassUpdateView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = StudyClass
    form_class = StudyClassForm
    template_name = "authority/add_class.html"
    success_url = reverse_lazy("authority:class_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Class"
        context["updated"] = True
        return context

    def form_valid(self, form):
        messages.success(self.request, "Class Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class DeleteStudyClassView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model = StudyClass
    context_object_name = "student_class"
    template_name = "authority/delete_class.html"
    success_url = reverse_lazy("authority:class_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Class"
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)
