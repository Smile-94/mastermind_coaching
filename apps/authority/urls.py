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
from apps.authority.views.manage_class import (
    StudyClassInfoView,
    StudyClassUpdateView,
    DeleteStudyClassView,
)

from apps.authority.views.manage_instituate import (
    InstituteInfoView,
    InstituteUpdateView,
    DeleteInstituteView,
)

from apps.authority.views.student_profile import (
    AddStudentView,
    StudentDetailView,
    UpdateStudentView,
    StudentListView,
    DeleteStudentView,
    AddUpdateStudentInfoView,
)

from apps.authority.views.manage_notice import (
    AddNoticeView,
    NoticeListView,
    UpdateNoticeView,
    NoticeDetailView,
    DeleteTeacherView,
)

from apps.authority.views.week_days import (
    WeekDaysInfoView,
    WeekDaysUpdateView,
    DeleteWeekDaysView,
)

from apps.authority.views.manage_course import (
    CourseInfoView,
    CourseUpdateView,
    DeleteCourseDaysView,
)

from apps.authority.views.manage_batch import (
    AddBatchView,
    BatchListView,
    BatchDetailView,
    UpdateBatchView,
    DeleteBatchView,
)  # update batch url

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

# Manage class
urlpatterns += [
    path("add-class/", StudyClassInfoView.as_view(), name="class_info"),
    path(
        "update-class/<int:pk>/", StudyClassUpdateView.as_view(), name="update_class"
    ),  # update class url
    path(
        "delete-class/<int:pk>/", DeleteStudyClassView.as_view(), name="delete_class"
    ),  # delete class url
]

# Manage institute
urlpatterns += [
    path("add-institute/", InstituteInfoView.as_view(), name="institute_info"),
    path(
        "update-institute/<int:pk>/",
        InstituteUpdateView.as_view(),
        name="update_institute",
    ),  # update institute url
    path(
        "delete-institute/<int:pk>/",
        DeleteInstituteView.as_view(),
        name="delete_institute",
    ),  # delete institute url
]

# Manage student
urlpatterns += [
    path("add-student/", AddStudentView.as_view(), name="add_student"),
    path("student-list/", StudentListView.as_view(), name="student_list"),
    path(
        "update-student/<int:pk>/", UpdateStudentView.as_view(), name="update_student"
    ),  # update student url
    path(
        "student-details/<int:pk>/", StudentDetailView.as_view(), name="student_details"
    ),  # student detail url
    path(
        "delete-student/<int:pk>/", DeleteStudentView.as_view(), name="delete_student"
    ),  # delete student url
    path(
        "add-update-student-info/<int:pk>/",
        AddUpdateStudentInfoView.as_view(),
        name="add_update_student_info",
    ),  # add update student info url
]

# Manage notice
urlpatterns += [
    path("add-notice/", AddNoticeView.as_view(), name="add_notice"),
    path("notice-list/", NoticeListView.as_view(), name="notice_list"),
    path(
        "update-notice/<int:pk>/", UpdateNoticeView.as_view(), name="update_notice"
    ),  # update notice url
    path(
        "notice-details/<int:pk>/", NoticeDetailView.as_view(), name="notice_details"
    ),  # notice detail url
    path(
        "delete-notice/<int:pk>/", DeleteTeacherView.as_view(), name="delete_notice"
    ),  # delete notice url
]


# Manage week days
urlpatterns += [
    path("add-week-days/", WeekDaysInfoView.as_view(), name="week_days"),
    path(
        "update-week-days/<int:pk>/",
        WeekDaysUpdateView.as_view(),
        name="update_week_days",
    ),  # update week days url
    path(
        "delete-week-days/<int:pk>/",
        DeleteWeekDaysView.as_view(),
        name="delete_week_days",
    ),  # delete week days url
]

# Manage course
urlpatterns += [
    path("add-course/", CourseInfoView.as_view(), name="course_info"),
    path(
        "update-course/<int:pk>/", CourseUpdateView.as_view(), name="update_course"
    ),  # update course url
    path(
        "delete-course/<int:pk>/",
        DeleteCourseDaysView.as_view(),
        name="delete_course",
    ),  # delete course days url
]

# Manage batch
urlpatterns += [
    path("add-batch/", AddBatchView.as_view(), name="add_batch"),
    path("batch-list/", BatchListView.as_view(), name="batch_list"),
    path("batch-details/<int:pk>/", BatchDetailView.as_view(), name="batch_details"),
    path(
        "update-batch/<int:pk>/", UpdateBatchView.as_view(), name="update_batch"
    ),  # update batch url
    path(
        "delete-batch/<int:pk>/", DeleteBatchView.as_view(), name="delete_batch"
    ),  # delete batch url
]  # update batch url
