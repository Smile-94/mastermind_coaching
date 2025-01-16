from django.http import JsonResponse

# class Based View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from apps.authority.models.course_model import EnrolledStudent, Batch
from apps.authority.forms.course_form import EnrolledStudentForm
from apps.student.models.student_model import StudentProfile

# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# Filters
from apps.authority.filters.course_filter import BatchFilter


class CourseEnrollmentListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Batch
    queryset = Batch.objects.filter(is_active=True).order_by("-id")
    filterset_class = BatchFilter
    template_name = "authority/course/enrolment_batch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enrollment List"
        context["batch_list"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context


class EnrollStudentCreateView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = EnrolledStudent
    form_class = EnrolledStudentForm
    template_name = "authority/course/course_enrollment.html"
    success_url = reverse_lazy(
        "authority:course_enrollment"
    )  # Replace with your success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enrolled Student"
        return context

    def form_valid(self, form):
        student_id = form.cleaned_data["enrolled_student"]
        batch = self.kwargs["batch"]

        # Check if the batch exists
        if not Batch.objects.filter(id=batch).exists():
            messages.error(self.request, "Batch does not exist.")
            return self.form_invalid(form)

        enroll_batch = Batch.objects.get(id=batch)

        # Check if the student exists
        if not student_id:
            messages.error(self.request, "Student does not exist.")
            return self.form_invalid(form)

        # Check if the student is already enrolled in the same class
        if EnrolledStudent.objects.filter(
            enrolled_batch=enroll_batch,
            enrolled_student_id=student_id,
        ).exists():
            messages.error(self.request, "Student is already enrolled in this class.")
            return self.form_invalid(form)

        # if self.model.objects.filter(enrolled_student=student_id, enrolled_batch__student_class=).exists():

        # Check for conflicting batches
        conflicting_batches = EnrolledStudent.objects.filter(
            enrolled_student=student_id,
            enrolled_batch__course=enroll_batch.course,
            enrolled_batch__start_date__lte=enroll_batch.end_date,
            enrolled_batch__end_date__gte=enroll_batch.start_date,
        ).exclude(enrolled_batch=enroll_batch)

        if conflicting_batches.exists():
            messages.error(
                self.request,
                "Conflict detected. The student is already enrolled in another batch for the same course during overlapping dates.",
            )
            return self.form_invalid(form)

        # If all validations pass, save the form and return success response
        if form.is_valid():
            enrolled = form.save(commit=False)
            enrolled.enrolled_batch = enroll_batch
            enrolled.save()
            messages.success(self.request, "Student Enrolled Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)
