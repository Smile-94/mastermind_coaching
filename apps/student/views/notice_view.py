from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.student.permission import StudentPassesTestMixin

# class Based View
from django.views.generic import ListView
from django.views.generic import DetailView


# Models
from apps.authority.models.notice_model import (
    Notice,
    PublishedStatusChoice,
    NoticePublishedForChoice,
)


# Import Filter
from apps.authority.filters.notice_filter import NoticeFilter


class StudentNoticeListView(LoginRequiredMixin, StudentPassesTestMixin, ListView):
    model = Notice
    queryset = queryset = Notice.objects.filter(
        Q(published_for=NoticePublishedForChoice.STUDENT)
        | Q(published_for=NoticePublishedForChoice.ALL),
        published_status=PublishedStatusChoice.PUBLISHED,
    ).order_by("-id")
    filterset_class = NoticeFilter
    template_name = "student/notice_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Notice List"
        context["notices"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context


class StudentNoticeDetailView(LoginRequiredMixin, StudentPassesTestMixin, DetailView):
    model = Notice
    context_object_name = "notice"
    template_name = "student/notice_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Notice Details"
        return context
