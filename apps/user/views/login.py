from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# class based view
from django.views import View
from django.contrib.auth.views import LogoutView

# login and logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# forms
from django.contrib.auth.forms import AuthenticationForm

# models
from apps.user.models import User, UserTypeChoice


# User Login Class
class UserLoginView(View):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("home:index")

    def get(self, request, *args, **kwargs):
        context_data = {"title": "Login", "form": self.form_class()}
        return render(request, self.template_name, context=context_data)

    def post(self, request, *args, **kwargs):
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            request_user = User.objects.get(username=username)

            if user is not None and request_user.user_type == UserTypeChoice.ADMIN:
                login(request, user)

                if "next" in request.POST:
                    redirect_url = request.POST.get("next")
                    return redirect(redirect_url)
                else:
                    messages.success(request, "Welcome to your user panel")
                    return HttpResponseRedirect(reverse("authority:authority_home"))

            elif user is not None and request_user.user_type == UserTypeChoice.STUDENT:
                login(request, user)
                messages.success(request, "Welcome to your user panel")
                # return HttpResponseRedirect(reverse("receptonist:receptonist"))
                return HttpResponse("We are working on Student panel")

            elif user is not None and request_user.user_type == UserTypeChoice.TEACHER:
                login(request, user)
                messages.success(request, "Welcome to your user panel")
                return HttpResponseRedirect(reverse("teacher:teacher_home"))
                # return HttpResponse("We are working on Teacher panel")

            else:
                messages.error(request, "User name or password invalid, try again!")
                # return redirect(reverse("accounts:login"))
                return HttpResponse("User name or password invalid, try again!")

        except Exception as e:
            print(e)
            messages.error(request, "User name or password invalid, try again!")
            return redirect(reverse("accounts:login"))


class UserLogoutView(LoginRequiredMixin, View):
    template_name = "accounts/login.html"
    extra_context = {"form": AuthenticationForm}

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("accounts:login"))
