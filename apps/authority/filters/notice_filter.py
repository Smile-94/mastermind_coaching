import django_filters
from django.db.models import Q
from apps.authority.models.notice_model import Notice


class NoticeFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    class Meta:
        model = Notice
        fields = [
            "query",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by title or published status matching the query keyword.
        """
        return queryset.filter(
            Q(title__icontains=value)
            | Q(published_status__icontains=value)
            | Q(published_for__icontains=value)
        )
