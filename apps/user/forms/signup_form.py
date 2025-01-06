from django.forms import CharField, EmailField, TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm

# models
from apps.user.models import User


# forms
class SignUpForm(UserCreationForm):
    name = CharField(
        max_length=100,
        widget=TextInput(attrs={"class": "form-control", "placeholder": "John Doe"}),
    )
    email = EmailField(
        required=False,
        widget=EmailInput(
            attrs={"class": "form-control", "placeholder": "example@example.com"}
        ),
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": "Test123@"}
        ),
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": "Test123@"}
        ),
    )
    phone = CharField(
        max_length=15,
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Phone Number i,e +8801921000000",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "name", "phone")
