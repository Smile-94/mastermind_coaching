from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.contrib import messages

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# Filters
from apps.authority.filters.course_filter import WeekDaysFilter

# Generics Views
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Models
from apps.authority.models.course_model import WeekDays

# Forms
from apps.authority.forms.course_form import WeekDaysForm


class WeekDaysInfoView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = WeekDays
    queryset = WeekDays.objects.filter(is_active=True)
    form_class = WeekDaysForm
    filterset_class = WeekDaysFilter
    template_name = "authority/course/add_week_days.html"
    success_url = reverse_lazy("authority:week_days")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Week Days"
        context["week_days"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context

    def form_valid(self, form):
        messages.success(self.request, "Week Day Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class WeekDaysUpdateView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = WeekDays
    form_class = WeekDaysForm
    template_name = "authority/course/add_week_days.html"
    success_url = reverse_lazy("authority:week_days")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Week Days"
        context["updated"] = True
        return context

    def form_valid(self, form):
        messages.success(self.request, "Day Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class DeleteWeekDaysView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model = WeekDays
    context_object_name = "object"
    template_name = "authority/course/delete_week_days.html"
    success_url = reverse_lazy("authority:week_days")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Week Day"
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)
