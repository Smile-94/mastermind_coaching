from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Import drf-spectacular Class
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps.endpoint import urls as end_points
# PRE_URL = "auth-service/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(end_points)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    # YOUR PATTERNS
    path("/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "care-box-docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redocs/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

# debug toolbar for local and development
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
