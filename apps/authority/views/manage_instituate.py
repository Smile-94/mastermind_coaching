from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.contrib import messages

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# Filters
from apps.authority.filters.study_class_filter import InstituteFilter

# Generics Views
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Models
from apps.authority.models.class_model import Institute

# Forms
from apps.authority.forms.class_form import InstituteForm


class InstituteInfoView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Institute
    queryset = Institute.objects.filter(is_active=True)
    form_class = InstituteForm
    filterset_class = InstituteFilter
    template_name = "authority/add_institute.html"
    success_url = reverse_lazy("authority:institute_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Class"
        context["institutes"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context

    def form_valid(self, form):
        messages.success(self.request, "Institute Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class InstituteUpdateView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Institute
    form_class = InstituteForm
    template_name = "authority/add_institute.html"
    success_url = reverse_lazy("authority:institute_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Institute Information"
        context["updated"] = True
        return context

    def form_valid(self, form):
        messages.success(self.request, "Institute Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class DeleteInstituteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model = Institute
    context_object_name = "institute"
    template_name = "authority/delete_institute.html"
    success_url = reverse_lazy("authority:institute_info")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Institute"
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)
