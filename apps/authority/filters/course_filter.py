import django_filters
from django.db.models import Q
from apps.authority.models.course_model import Course, Batch, WeekDays


class WeekDaysFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    # s_holiday = django_filters.BooleanFilter(field_name="is_holiday", label="Is Holiday")
    class Meta:
        model = WeekDays
        fields = [
            "query",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by title or published status matching the query keyword.
        """
        return queryset.filter(Q(days__icontains=value))


class CourseFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    class Meta:
        model = Course
        fields = [
            "query",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by title or published status matching the query keyword.
        """
        return queryset.filter(
            Q(course_name__icontains=value) | Q(course_code__icontains=value)
        )


class BatchFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    class Meta:
        model = Batch
        fields = [
            "query",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by title or published status matching the query keyword.
        """
        return queryset.filter(Q(batch_name__icontains=value))
