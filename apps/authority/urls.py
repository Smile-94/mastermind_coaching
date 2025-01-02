from django.urls import path

from apps.authority.views.home import AdminHomeView
from apps.authority.views.teacher_profile import AddTeacherView

app_name = "authority"

# views


urlpatterns = [
    path("", AdminHomeView.as_view(), name="authority_home"),  # authority home url
    path("add_teacher/", AddTeacherView.as_view(), name="add_teacher"),
]
