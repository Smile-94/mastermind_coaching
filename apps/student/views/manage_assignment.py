from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin


# custom UserpassTestMixin
from apps.student.permission import StudentPassesTestMixin

# class Based View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Models
from apps.authority.models.course_model import (
    Assignment,
    Batch,
    SubmittedAssignment,
    EnrolledStudent,
)


# forms
from apps.authority.forms.assignment_form import AssignmentForm
from apps.authority.forms.course_form import SubmittedAssignmentForm


# Filters
from apps.authority.filters.course_filter import AssignmentFilter


class StudentAssignmentListView(LoginRequiredMixin, StudentPassesTestMixin, ListView):
    model = Assignment
    queryset = Assignment.objects.all()
    filterset_class = AssignmentFilter
    template_name = "student/assignment_list.html"

    def get_context_data(self, **kwargs):
        student = EnrolledStudent.objects.get(
            enrolled_student=self.request.user.student_profile
        )
        context = super().get_context_data(**kwargs)
        context["title"] = "Assignment List"
        context["objects"] = self.filterset_class(
            self.request.GET,
            queryset=self.queryset.filter(
                batch__enrolled_batch__enrolled_student=self.request.user.student_profile
            ),
        )
        context["is_submitted"] = SubmittedAssignment.objects.filter(
            submitted_student=student
        ).exists()
        return context


class StudentAssignmentDetailView(
    LoginRequiredMixin, StudentPassesTestMixin, DetailView
):
    model = Assignment
    context_object_name = "object"
    template_name = "student/assignment_details.html"

    def get_context_data(self, **kwargs):
        student = EnrolledStudent.objects.get(
            enrolled_student=self.request.user.student_profile
        )
        context = super().get_context_data(**kwargs)
        context["title"] = "Assignment Details"
        context["is_submitted"] = SubmittedAssignment.objects.filter(
            submitted_student=student
        ).exists()
        return context
        return context


class CreateSubmittedAssignmentView(
    LoginRequiredMixin, StudentPassesTestMixin, CreateView
):
    model = SubmittedAssignment
    form_class = SubmittedAssignmentForm
    template_name = "student/submit_assignment.html"

    def get_object(self, queryset=None):
        """
        Override get_object to explicitly fetch the model instance.
        """
        pk = self.kwargs.get("pk")  # Assuming `pk` is passed as a URL parameter
        return Assignment.objects.get(pk=pk)

    def get_success_url(self):
        """
        Dynamically generate the success URL using the object's related assignment's primary key.
        """

        return reverse_lazy(
            "student:student_assignment_details",
            kwargs={"pk": self.get_object().pk},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["title"] = "Graded Assignment"
            context["is_update"] = True
            context["object"] = self.get_object()
        except Exception as e:
            print(e)
        return context

    def form_valid(self, form):
        try:
            if form.is_valid():
                if EnrolledStudent.objects.filter(
                    enrolled_student=self.request.user.student_profile
                ).exists():
                    student = EnrolledStudent.objects.get(
                        enrolled_student=self.request.user.student_profile
                    )
                    print(student)
                assignment = form.save(commit=False)
                assignment.submitted_student = student
                assignment.assignment = self.get_object()
                assignment.save()
                # Redirect to the assignment details page

            messages.success(self.request, "Assignment Submitted Successfully ")
            # return redirect(self.get_success_url())
            return super().form_valid(form)
        except Exception as e:
            print(e)
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"Failed to submit assignment: {str(form.errors)}")
        return super().form_invalid(form)


class UpdateSubmittedAssignmentView(
    LoginRequiredMixin, StudentPassesTestMixin, UpdateView
):
    model = SubmittedAssignment
    form_class = SubmittedAssignmentForm
    template_name = "student/update_assignment.html"
    success_url = reverse_lazy("teacher:teacher_assignment_list")

    def get_object(self, queryset=None):
        """
        Override get_object to explicitly fetch the model instance.
        """
        pk = self.kwargs.get("pk")  # Assuming `pk` is passed as a URL parameter
        return self.model.objects.get(pk=pk)

    def get_success_url(self):
        """
        Dynamically generate the success URL using the object's related assignment's primary key.
        """

        return reverse_lazy(
            "student:student_assignment_details",
            kwargs={"pk": self.get_object().assignment.pk},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context["title"] = "Graded Assignment"
            context["is_update"] = True
            context["object"] = self.get_object()

        except Exception as e:
            print(e)
        return context

    def post(self, request, *args, **kwargs):
        # Use get_object to fetch the instance and set self.object
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        try:
            # Save all valid forms in the formset
            form.save()
            messages.success(self.request, "Attendance taken successfully.")
            return redirect(
                "success_url"
            )  # Replace 'success_url' with your desired URL
        except Exception as e:
            messages.error(self.request, f"Error saving attendance: {e}")
            return redirect(
                "failure_url"
            )  # Replace 'failure_url' with your desired URL

    def form_invalid(self, form):
        messages.error(self.request, f"Failed to grade assignment: {form.errors}")
        return super().form_invalid(form)
