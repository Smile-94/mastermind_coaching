from django.urls import path
from django.contrib.auth import views as auth_views

from apps.user.views.login import UserLoginView

app_name = "accounts"

# views


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("", UserLoginView.as_view(), name="login"),
]
