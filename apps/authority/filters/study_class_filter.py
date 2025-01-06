import django_filters
from django.db.models import Q
from apps.authority.models.class_model import StudyClass, Institute


class StudyClassFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    class Meta:
        model = StudyClass
        fields = [
            "query",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by email or username matching the query keyword.
        """
        return queryset.filter(Q(class_name__icontains=value))


class InstituteFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    class Meta:
        model = Institute
        fields = [
            "query",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by email or username matching the query keyword.
        """
        return queryset.filter(Q(institute_name__icontains=value))
