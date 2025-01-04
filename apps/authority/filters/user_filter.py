import django_filters
from django.db.models import Q
from apps.user.models import User


class UserFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    class Meta:
        model = User
        fields = []

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by email or username matching the query keyword.
        """
        return queryset.filter(Q(email__icontains=value) | Q(username__icontains=value))
