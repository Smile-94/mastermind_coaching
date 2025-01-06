from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# class Based View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Models
from apps.authority.models.course_model import Batch


# forms
from apps.authority.forms.course_form import BatchForm


# Filters
from apps.authority.filters.course_filter import BatchFilter


class AddBatchView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Batch
    form_class = BatchForm
    template_name = "authority/course/add_batch.html"
    success_url = reverse_lazy("authority:batch_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Student"
        return context

    def form_valid(
        self,
        form,
    ):
        if form.is_valid():
            messages.success(self.request, "Batch Created Success Fully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class BatchListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Batch
    queryset = Batch.objects.filter(is_active=True).order_by("-id")
    filterset_class = BatchFilter
    template_name = "authority/course/batch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Batch List"
        context["batch_list"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context


class BatchDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = Batch
    context_object_name = "object"
    template_name = "authority/course/batch_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Batch Details"
        return context


class UpdateBatchView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Batch
    form_class = BatchForm
    template_name = "authority/course/update_batch.html"
    success_url = reverse_lazy("authority:batch_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["title"] = "Edit Batch Info"

        except Exception as e:
            print(e)
        return context

    def form_valid(self, form):
        try:
            if form.is_valid():
                messages.success(self.request, "Batch Info Updated Successfully")
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class DeleteBatchView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model = Batch
    context_object_name = "object"
    template_name = "authority/course/delete_batch.html"
    success_url = reverse_lazy("authority:batch_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Batch"
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)
