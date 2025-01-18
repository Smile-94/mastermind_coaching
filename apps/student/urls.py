from django.urls import path

from apps.student.views.student_main import StudentHomeView, StudentProfileView
from apps.student.views.notice_view import (
    StudentNoticeListView,
    StudentNoticeDetailView,
)
from apps.student.views.class_routine import StudentRoutineView
from apps.student.views.manage_assignment import (
    StudentAssignmentListView,
    StudentAssignmentDetailView,
    CreateSubmittedAssignmentView,
    UpdateSubmittedAssignmentView,
)
from apps.student.views.enrolled_course import StudentCourseEnrollmentView

app_name = "student"

urlpatterns = [
    path("", StudentHomeView.as_view(), name="student_home"),  # student home url
    path(
        "profile/", StudentProfileView.as_view(), name="student_profile"
    ),  # student profile url
]

# Notice
urlpatterns += [
    path(
        "notices/", StudentNoticeListView.as_view(), name="student_notice_list"
    ),  # notice list url
    path(
        "notices/<int:pk>/",
        StudentNoticeDetailView.as_view(),
        name="student_notice_details",
    ),  # notice details url
]

# Class Routine
urlpatterns += [
    path(
        "class-routine/", StudentRoutineView.as_view(), name="student_class_routine"
    ),  # class routine url
]


# Manage Assignment
urlpatterns += [
    path(
        "assignments/",
        StudentAssignmentListView.as_view(),
        name="student_assignment_list",
    ),  # assignment list url
    path(
        "assignment-details/<int:pk>/",
        StudentAssignmentDetailView.as_view(),
        name="student_assignment_details",
    ),  # assignment detail url
    path(
        "submit-assignment/<int:pk>/",
        CreateSubmittedAssignmentView.as_view(),
        name="submit_assignment",
    ),  # submit assignment url
    path(
        "update-submitted-assignment/<int:pk>/",
        UpdateSubmittedAssignmentView.as_view(),
        name="update_submitted_assignment",
    ),  # update submitted assignment url
]

# Enrolled Course
urlpatterns += [
    path(
        "enrolled-course/",
        StudentCourseEnrollmentView.as_view(),
        name="student_enrolled_course",
    ),  # enrolled course url
]
