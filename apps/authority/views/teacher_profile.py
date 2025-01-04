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
from apps.teacher.models.profile_model import (
    TeacherProfile,
    Address,
    EducationalQualification,
)
from common.models import UserTypeChoice

# forms
from apps.user.forms.signup_form import SignUpForm
from apps.user.forms.update_form import UpdateUserForm
from apps.teacher.form.profile_form import (
    TeacherProfileForm,
    TeacherAddressForm,
    TeacherEducationForm,
)
# from accounts.forms import ProfileForm
# from accounts.forms import PresentAddressForm
# from accounts.forms import PermanentAddressForm
# from employee.forms import EmployeeInfoForm

# Filters
from apps.authority.filters.user_filter import UserFilter


class AddTeacherView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = "authority/add_teacher.html"
    success_url = reverse_lazy("authority:authority_home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Teacher"
        return context

    def form_valid(
        self,
        form,
    ):
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = UserTypeChoice.TEACHER
            user.save()
            messages.success(self.request, "Teacher Accounts Created Success Fully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class TeacherListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = User
    queryset = User.objects.filter(
        user_type=UserTypeChoice.TEACHER, is_active=True
    ).order_by("-id")
    filterset_class = UserFilter
    template_name = "authority/teacher_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Teacher List"
        context["users"] = self.filterset_class(
            self.request.GET, queryset=self.queryset
        )
        return context


class TeacherDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = User
    context_object_name = "user"
    template_name = "authority/teacher_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Teacher Details"
        return context


class AddUpdateTeacherInfoView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    form_class = TeacherProfileForm
    form_class2 = TeacherAddressForm
    template_name = "authority/add_teacher_info.html"
    success_url = reverse_lazy("authority:teacher_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_object = User.objects.get(id=self.kwargs.get("pk"))
            teacher_profile = TeacherProfile.objects.get_or_create(
                profile_of=user_object
            )
            teacher_address = Address.objects.get_or_create(address_of=user_object)
            context["title"] = "Add/Edit Employee Info"
            if teacher_profile:
                context["form"] = self.form_class(instance=user_object.teacher_profile)
            else:
                context["form"] = self.form_class()

            if teacher_address:
                context["form2"] = self.form_class2(
                    instance=user_object.teacher_address
                )

            else:
                context["form2"] = self.form_class2()
        except Exception as e:
            print(e)
        return context

    def post(self, request, *args, **kwargs):
        user_object = User.objects.get(id=self.kwargs.get("pk"))
        form = self.form_class(
            request.POST, request.FILES, instance=user_object.teacher_profile
        )
        form2 = self.form_class2(request.POST, instance=user_object.teacher_address)
        return self.form_valid(form, form2)

    def form_valid(self, form, form2):
        try:
            if form.is_valid() and form2.is_valid():
                user = form.save(commit=False)
                info = form2.save(commit=False)
                user.profile_of = User.objects.get(id=self.kwargs.get("pk"))
                info.address_of = User.objects.get(id=self.kwargs.get("pk"))
                user.save()
                info.save()
                messages.success(self.request, "Employee Info Updated Successfully")
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Some thing wrong try again")
        return super().form_invalid(form)


class UpdateTeacherView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = "authority/update_teacher.html"
    success_url = reverse_lazy("authority:teacher_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_object = User.objects.get(id=self.kwargs.get("pk"))

            context["title"] = "Add/Edit Teacher Account Info"
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
                messages.success(self.request, "Teacher Info Updated Successfully")
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class AddTeacherEducationView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    form_class = TeacherEducationForm
    template_name = "authority/add_teacher_education.html"
    success_url = reverse_lazy("authority:teacher_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_object = User.objects.get(id=self.kwargs.get("pk"))
            teacher_education = EducationalQualification.objects.get_or_create(
                teacher=user_object
            )
            context["title"] = "Add/Edit Teacher Educational Info"
            context["name"] = user_object.name
            if teacher_education:
                context["form"] = self.form_class(instance=user_object.qualifications)
            else:
                context["form"] = self.form_class()

        except Exception as e:
            print(e)
        return context

    def post(self, request, *args, **kwargs):
        user_object = User.objects.get(id=self.kwargs.get("pk"))
        # teacher_education = EducationalQualification.objects.get_or_create(
        #     teacher=user_object
        # )
        form = self.form_class(request.POST, instance=user_object.qualifications)

        return self.form_valid(form)

    def form_valid(self, form):
        try:
            if form.is_valid():
                messages.success(
                    self.request, "Teacher Educational Info Updated Successfully"
                )
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"{form.errors}")
        return super().form_invalid(form)


class DeleteTeacherView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model = User
    context_object_name = "user"
    template_name = "authority/delete_teacher.html"
    success_url = reverse_lazy("authority:teacher_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Teacher"
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)
