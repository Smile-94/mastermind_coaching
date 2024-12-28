from django.urls import include, path

# Import Url
from apps.user.url import account_url


urlpatterns = [
    path("", include(account_url)),  # account endpoints
]
