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
from apps.authority.models.notice_model import Notice, PublishedStatusChoice

# forms
from apps.authority.forms.notice_form import NoticeForm

# Import Filter
from apps.authority.filters.notice_filter import NoticeFilter


class AddNoticeView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = "authority/add_notice.html"
    success_url = reverse_lazy("authority:notice_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Notice"
        return context

    def form_valid(
        self,
        form,
    ):
        if form.is_valid():
            messages.success(self.request, "Notice Created Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class NoticeListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Notice
    queryset = queryset = Notice.objects.exclude(
        published_status=PublishedStatusChoice.ARCHIVED
    ).order_by("-id")
    filterset_class = NoticeFilter
    template_name = "authority/notice_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Notice List"
        context["notices"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context


class NoticeDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = Notice
    context_object_name = "notice"
    template_name = "authority/notice_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Notice Details"
        return context


class UpdateNoticeView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = "authority/update_notice.html"
    success_url = reverse_lazy("authority:notice_list")

    def get_object(self, queryset=None):
        """
        Override get_object to explicitly fetch the model instance.
        """
        pk = self.kwargs.get("pk")  # Assuming `pk` is passed as a URL parameter
        return self.model.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["title"] = "Update Notice"
        except Exception as e:
            print(e)
        return context

    def post(self, request, *args, **kwargs):
        # Use get_object to fetch the instance
        instance = self.get_object()
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        try:
            messages.success(self.request, "Updated Notice Successfully")
            return super().form_valid(form)
        except Exception as e:
            print(e)
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class DeleteTeacherView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model = Notice
    context_object_name = "notice"
    template_name = "authority/delete_notice.html"
    success_url = reverse_lazy("authority:notice_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Notice"
        return context

    def form_valid(self, form):
        self.object.published_status = PublishedStatusChoice.ARCHIVED
        self.object.save()
        return redirect(self.success_url)
