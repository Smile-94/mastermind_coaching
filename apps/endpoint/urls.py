from django.urls import include, path

# Import Url
from apps.user.url import account_url
from apps.authority import urls as authority_urls
from apps.teacher import urls as teacher_urls


urlpatterns = [
    path("", include(account_url)),  # account endpoints
    path("authority/", include(authority_urls)),  # admin endpoints
    path("teacher/", include(teacher_urls)),  # teacher endpoints
]
