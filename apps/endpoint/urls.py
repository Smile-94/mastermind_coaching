from django.urls import include, path

# Import Url
from apps.user.url import account_url
from apps.authority import urls as authority_urls


urlpatterns = [
    path("", include(account_url)),  # account endpoints
    path("authority/", include(authority_urls)),  # admin endpoints
]
