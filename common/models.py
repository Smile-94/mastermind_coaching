from datetime import datetime

from django.db.models import Model, DateTimeField, TextChoices
from pydantic import BaseModel, PositiveInt, field_serializer


class DjangoBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserTypeChoice(TextChoices):
    ADMIN = "admin", "Admin"
    TEACHER = "teacher", "Teacher"
    STUDENT = "student", "Student"


class ActiveStatusChoice(TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"


class Payload(BaseModel):
    claim_id: str | None
    user_id: PositiveInt
    username: str
    client_id: str
    claim_time: datetime
    exp: datetime

    def is_valid(self):
        return self.exp > datetime.now()

    @field_serializer("claim_time", "exp", return_type=str, when_used="always")
    def date_time_serializer(self, value):
        return str(value)
