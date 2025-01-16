from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin


# custom UserpassTestMixin
from apps.teacher.permission import TeacherPassesTestMixin

# class Based View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Models
from apps.authority.models.course_model import Assignment, Batch


# forms
from apps.authority.forms.assignment_form import AssignmentForm


# Filters
from apps.authority.filters.course_filter import AssignmentFilter


class AddAssignmentView(LoginRequiredMixin, TeacherPassesTestMixin, CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "teacher/add_assignment.html"
    success_url = reverse_lazy("teacher:teacher_course_enrollment")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Assignment"
        return context

    def form_valid(self, form, *args, **kwargs):
        try:
            batch = Batch.objects.get(id=self.kwargs.get("course_id"))
        except Exception as e:
            print(e)
            messages.error(self.request, "Batch Not Found")
            return redirect("teacher:teacher_home")

        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.batch = batch
            assignment.save()
            messages.success(self.request, "Assignment Created Success Fully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class TeacherAssignmentListView(LoginRequiredMixin, TeacherPassesTestMixin, ListView):
    model = Assignment
    queryset = Assignment.objects.all()
    filterset_class = AssignmentFilter
    template_name = "teacher/assignment_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Assignment List"
        context["objects"] = self.filterset_class(
            self.request.GET,
            queryset=self.queryset.filter(
                batch__course_instructor=self.request.user.teacher_profile
            ),
        )
        return context


class TeacherAssignmentDetailView(
    LoginRequiredMixin, TeacherPassesTestMixin, DetailView
):
    model = Assignment
    context_object_name = "object"
    template_name = "teacher/assignment_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Assignment Details"
        return context


class UpdateAssignmentView(LoginRequiredMixin, TeacherPassesTestMixin, UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "teacher/add_assignment.html"
    success_url = reverse_lazy("teacher:teacher_assignment_list")

    def get_object(self, queryset=None):
        """
        Override get_object to explicitly fetch the model instance.
        """
        pk = self.kwargs.get("pk")  # Assuming `pk` is passed as a URL parameter
        return self.model.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["title"] = "Update Assignment"
            context["is_update"] = True
        except Exception as e:
            print(e)
        return context

    def post(self, request, *args, **kwargs):
        # Use get_object to fetch the instance
        instance = self.get_object()
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        try:
            messages.success(self.request, "Updated Assignment Successfully")
            return super().form_valid(form)
        except Exception as e:
            print(e)
            return super().form_invalid(form)


class DeleteAssignmentView(LoginRequiredMixin, TeacherPassesTestMixin, DeleteView):
    model = Assignment
    context_object_name = "object"
    template_name = "teacher/delete_assignment.html"
    success_url = reverse_lazy("teacher:teacher_assignment_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Assignment"
        return context

    def form_valid(self, form):
        self.object.delete()
        messages.success(self.request, "Assignment deleted successfully.")
        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(self.request, f"Failed to delete assignment {form.errors}")
        super().form_invalid(form)
