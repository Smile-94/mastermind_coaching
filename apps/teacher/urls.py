from django.urls import path

from apps.teacher.views.teacher_main import TeacherHomeView, TeacherProfileView
from apps.teacher.views.notice_view import (
    TeacherNoticeListView,
    TeacherNoticeDetailView,
)


app_name = "teacher"

urlpatterns = [
    path("", TeacherHomeView.as_view(), name="teacher_home"),  # teacher home url
    path(
        "profile/", TeacherProfileView.as_view(), name="teacher_profile"
    ),  # teacher profile url
]

urlpatterns += [
    path("notices/", TeacherNoticeListView.as_view(), name="teacher_notice_list"),
    path(
        "notices/<int:pk>/",
        TeacherNoticeDetailView.as_view(),
        name="teacher_notice_details",
    ),
]
