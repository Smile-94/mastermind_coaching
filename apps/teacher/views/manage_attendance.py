from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from django.forms import modelformset_factory
from apps.authority.models.course_model import Batch, Attendance, EnrolledStudent
from apps.authority.forms.course_form import AttendanceForm
from apps.teacher.permission import TeacherPassesTestMixin
from django.urls import reverse
from django.urls import reverse_lazy

# class Based View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from apps.authority.filters.course_filter import AttendanceFilter


class TakeAttendanceView(LoginRequiredMixin, TeacherPassesTestMixin, View):
    model = Attendance
    template_name = "teacher/add_attendance.html"
    batch = None
    date = None
    is_taken = False

    def dispatch(self, request, *args, **kwargs):
        self.batch = get_object_or_404(Batch, id=self.kwargs["batch_id"])
        self.date = self.request.GET.get("attendance_date", now().date())
        self.is_taken = Attendance.objects.filter(
            batch=self.batch, attendance_date=self.date
        ).exists()
        return super().dispatch(request, *args, **kwargs)

    def get_formset(self, data=None):
        attendance_qs = Attendance.objects.filter(
            batch=self.batch, attendance_date=self.date
        )
        if not attendance_qs.exists():
            enrolled_students = EnrolledStudent.objects.filter(
                enrolled_batch=self.batch
            )
            Attendance.objects.bulk_create(
                [
                    Attendance(
                        batch=self.batch,
                        student=student.enrolled_student,
                        attendance_date=self.date,
                        is_present=False,
                    )
                    for student in enrolled_students
                    if student.enrolled_student
                ]
            )
            attendance_qs = Attendance.objects.filter(
                batch=self.batch, attendance_date=self.date
            )

        AttendanceFormSet = modelformset_factory(
            Attendance, form=AttendanceForm, extra=0
        )
        return AttendanceFormSet(data, queryset=attendance_qs)

    def get_context_data(self, **kwargs):
        context = {
            "batch": self.batch,
            "date": self.date,
            "is_taken": self.is_taken,
            "formset": self.get_formset()
            if "formset" not in kwargs
            else kwargs["formset"],
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        print("Formset: ", formset)
        if formset.is_valid():
            return self.form_valid(formset)

        return self.form_invalid(formset)

    def form_valid(self, formset):
        try:
            formset.save()
        except Exception as e:
            print(e)
        messages.success(self.request, "Attendance taken successfully.")
        return redirect(
            reverse("teacher:take_attendance", kwargs={"batch_id": self.batch.pk})
        )

    def form_invalid(self, formset):
        messages.error(self.request, f"Failed to take attendance: {formset.errors}")
        return redirect(
            reverse("teacher:take_attendance", kwargs={"batch_id": self.batch.pk})
        )


class TeacherAttendanceListView(LoginRequiredMixin, TeacherPassesTestMixin, ListView):
    model = Attendance
    queryset = Attendance.objects.all()
    filterset_class = AttendanceFilter
    template_name = "teacher/attendance_list.html"

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


class UpdateAttendanceView(LoginRequiredMixin, TeacherPassesTestMixin, UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "teacher/update_attendance.html"
    success_url = reverse_lazy("teacher:teacher_attendance_list")

    def get_object(self, queryset=None):
        """
        Override get_object to explicitly fetch the model instance.
        """
        pk = self.kwargs.get("pk")  # Assuming `pk` is passed as a URL parameter
        return self.model.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["title"] = "Update Attendance"
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
            messages.success(self.request, "Updated Attendance Successfully")
            return super().form_valid(form)
        except Exception as e:
            print(e)
            return super().form_invalid(form)
