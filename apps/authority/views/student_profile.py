from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from apps.authority.permission.admin_permission import AdminPassesTestMixin

# class Based View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Models
from apps.user.models import User
from apps.student.models.student_model import StudentProfile
from common.models import UserTypeChoice
from apps.authority.models.course_model import Batch

# forms
from apps.user.forms.signup_form import SignUpForm
from apps.user.forms.update_form import UpdateUserForm
from apps.student.forms.profile_form import StudentProfileForm
# from accounts.forms import ProfileForm
# from accounts.forms import PresentAddressForm
# from accounts.forms import PermanentAddressForm
# from employee.forms import EmployeeInfoForm

# Filters
from apps.authority.filters.user_filter import UserFilter


class AddStudentView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = "authority/add_student.html"
    success_url = reverse_lazy("authority:student_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Student"
        return context

    def form_valid(
        self,
        form,
    ):
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = UserTypeChoice.STUDENT
            user.save()
            messages.success(self.request, "Student Accounts Created Success Fully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class StudentListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = User
    queryset = User.objects.filter(
        user_type=UserTypeChoice.STUDENT, is_active=True
    ).order_by("-id")
    filterset_class = UserFilter
    template_name = "authority/student_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Student List"
        context["users"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context


class StudentDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = User
    context_object_name = "user"
    template_name = "authority/student_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Teacher Details"
        return context


class AddUpdateStudentInfoView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    form_class = StudentProfileForm
    template_name = "authority/add_student_info.html"
    success_url = reverse_lazy("authority:student_list")

    def get_object(self, queryset=None):
        """Get or create the StudentProfile instance for the user."""
        user = User.objects.get(id=self.kwargs.get("pk"))
        student_profile, created = StudentProfile.objects.get_or_create(
            student_user=user
        )
        return student_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add/Edit Student Info"
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Set the `object` explicitly
        form = self.form_class(request.POST, request.FILES, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Student Profile Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


# class AddUpdateStudentInfoView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
#     model = User
#     form_class = StudentProfileForm
#     template_name = "authority/add_student_info.html"
#     success_url = reverse_lazy("authority:student_list")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             user_object = User.objects.get(id=self.kwargs.get("pk"))
#             student_profile = StudentProfile.objects.get_or_create(
#                 student_user=user_object
#             )
#             context["title"] = "Add/Edit Student Info"
#             if student_profile:
#                 context["form"] = self.form_class(instance=user_object.student_profile)
#             else:
#                 context["form"] = self.form_class()

#         except Exception as e:
#             print("error: ", e)
#         return context

#     def post(self, request, *args, **kwargs):
#         user_object = User.objects.get(id=self.kwargs.get("pk"))
#         # teacher_education = EducationalQualification.objects.get_or_create(
#         #     teacher=user_object
#         # )
#         form = self.form_class(request.POST, instance=user_object.student_profile)
#         print("Post Form: ", form)
#         return self.form_valid(form)

#     def form_valid(self, form):
#         try:
#             if form.is_valid():
#                 messages.success(
#                     self.request, "Teacher Educational Info Updated Successfully"
#                 )
#             return super().form_valid(form)

#         except Exception as e:
#             print("Form validation error: ", e)
#             return super().form_invalid(form)

#     def form_invalid(self, form):
#         messages.error(self.request, f"{form.errors}")
#         return super().form_invalid(form)


class UpdateStudentView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = "authority/update_student.html"
    success_url = reverse_lazy("authority:student_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_object = User.objects.get(id=self.kwargs.get("pk"))

            context["title"] = "Add/Edit Student Account Info"
            context["form"] = self.form_class(instance=user_object)

        except Exception as e:
            print(e)
        return context

    def post(self, request, *args, **kwargs):
        user_object = User.objects.get(id=self.kwargs.get("pk"))
        form = self.form_class(request.POST, instance=user_object)
        return self.form_valid(form)

    def form_valid(self, form):
        try:
            if form.is_valid():
                messages.success(self.request, "Student Info Updated Successfully")
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class DeleteStudentView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model = User
    context_object_name = "user"
    template_name = "authority/delete_student.html"
    success_url = reverse_lazy("authority:student_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Student"
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)


class StudentEnrolledCourseView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Batch
    queryset = Batch.objects.filter(
        is_active=True,
    ).order_by("-id")
    template_name = "authority/course/enrolled_course.html"

    def get_context_data(self, **kwargs):
        try:
            student = StudentProfile.objects.get(id=self.kwargs.get("pk"))
        except Exception as e:
            print(e)
        context = super().get_context_data(**kwargs)
        context["title"] = "Enrollment List"
        if student:
            context["batch_list"] = self.queryset.filter(
                enrolled_batch__enrolled_student=student
            )
        context["student"] = student
        return context
