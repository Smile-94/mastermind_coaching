import django_filters
from django.db.models import Q
from apps.authority.models.course_model import (
    Course,
    Batch,
    WeekDays,
    EnrolledStudent,
    Assignment,
    Attendance,
)
from django.forms import DateInput


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


#
class EnrolledStudentFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    class Meta:
        model = EnrolledStudent
        fields = [
            "query",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by title or published status matching the query keyword.
        """
        return queryset.filter(
            Q(enrolled_student__student_user__name__icontains=value)
            | Q(enrolled_student__student_user__username__icontains=value)
        )


class AssignmentFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")

    class Meta:
        model = Assignment
        fields = [
            "query",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by title or published status matching the query keyword.
        """
        return queryset.filter(
            Q(batch__batch_name__icontains=value) | Q(assignment_title__icontains=value)
        )


class AttendanceFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="filter_query", label="Search")
    attendance_date = django_filters.DateFilter(
        field_name="attendance_date",
        widget=DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    class Meta:
        model = Attendance
        fields = [
            "query",
            "attendance_date",
        ]

    def filter_query(self, queryset, name, value):
        """
        Filter the queryset by title or published status matching the query keyword.
        """
        return queryset.filter(
            Q(batch__batch_name__icontains=value)
            | Q(student__student_user__name__icontains=value)
            | Q(student__student_user__username__icontains=value)
        )
