from django.urls import path

from apps.teacher.views.teacher_main import TeacherHomeView, TeacherProfileView
from apps.teacher.views.notice_view import (
    TeacherNoticeListView,
    TeacherNoticeDetailView,
)

from apps.teacher.views.class_routine import TeacherRoutineView
from apps.teacher.views.course_enrollment import TeacherCourseEnrollmentView
from apps.teacher.views.manage_assignment import (
    AddAssignmentView,
    TeacherAssignmentListView,
    TeacherAssignmentDetailView,
    UpdateAssignmentView,
    DeleteAssignmentView,
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

urlpatterns += [
    path("class-routine/", TeacherRoutineView.as_view(), name="teacher_class_routine"),
]

# Course Enrollment
urlpatterns += [
    path(
        "course-enrollment/",
        TeacherCourseEnrollmentView.as_view(),
        name="teacher_course_enrollment",
    ),  # course enrollment list url
]

# Manage Assignment
urlpatterns += [
    path(
        "add-assignment/<int:course_id>/",
        AddAssignmentView.as_view(),
        name="add_assignment",
    ),  # add assignment url
    path(
        "assignments/",
        TeacherAssignmentListView.as_view(),
        name="teacher_assignment_list",
    ),  # assignment list url
    path(
        "assignment-details/<int:pk>/",
        TeacherAssignmentDetailView.as_view(),
        name="teacher_assignment_details",
    ),  # assignment detail url
    path(
        "update-assignment/<int:pk>/",
        UpdateAssignmentView.as_view(),
        name="update_assignment",
    ),  # update assignment url
    path(
        "delete-assignment/<int:pk>/",
        DeleteAssignmentView.as_view(),
        name="delete_assignment",
    ),  # delete assignment url
]
