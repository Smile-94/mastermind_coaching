from django.forms import ModelForm, ImageField, DateField, DateInput

# models
from apps.user.models import User


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "name",
            "email",
            "phone",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].disabled = True
