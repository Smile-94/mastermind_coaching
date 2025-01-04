from django.urls import path

from apps.authority.views.home import AdminHomeView
from apps.authority.views.teacher_profile import (
    AddTeacherView,
    TeacherListView,
    AddUpdateTeacherInfoView,
    UpdateTeacherView,
    AddTeacherEducationView,
    TeacherDetailView,
    DeleteTeacherView,
)

app_name = "authority"

# views


urlpatterns = [
    path("", AdminHomeView.as_view(), name="authority_home"),  # authority home url
    path("add_teacher/", AddTeacherView.as_view(), name="add_teacher"),
    path("teacher-list/", TeacherListView.as_view(), name="teacher_list"),
    path(
        "add-update-teacher-info/<int:pk>/",
        AddUpdateTeacherInfoView.as_view(),
        name="add_update_teacher_info",
    ),
    path(
        "update-teacher/<int:pk>/", UpdateTeacherView.as_view(), name="update_teacher"
    ),  # update teacher url
    path(
        "add-teacher-education/<int:pk>/",
        AddTeacherEducationView.as_view(),
        name="add_teacher_education",
    ),  # add teacher education url
    path(
        "teacher-details/<int:pk>/", TeacherDetailView.as_view(), name="teacher_details"
    ),  # teacher detail url
    path(
        "delete-teacher/<int:pk>/", DeleteTeacherView.as_view(), name="delete_teacher"
    ),  # delete teacher url
]
