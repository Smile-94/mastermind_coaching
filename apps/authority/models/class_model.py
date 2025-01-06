from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    BooleanField,
)
from common.models import DjangoBaseModel


class Institute(DjangoBaseModel):
    institute_name = CharField(max_length=250, unique=True)
    institute_address = CharField(max_length=250, blank=True, null=True)
    is_active = BooleanField(default=True, blank=True, null=True)

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        verbose_name = _("Institute")

    def __str__(self):
        return self.institute_name


class StudyClass(DjangoBaseModel):
    class_name = CharField(max_length=100, unique=True)
    is_active = BooleanField(default=True, blank=True, null=True)

    class Meta(DjangoBaseModel.Meta):
        ordering = ("-id",)
        verbose_name = _("Study Class")

    def __str__(self):
        return self.class_name
