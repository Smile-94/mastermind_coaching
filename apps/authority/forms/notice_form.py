from django.forms import ModelForm

# models
from apps.authority.models.notice_model import Notice


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"
