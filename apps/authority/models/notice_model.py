from django.db.models import (
    CharField,
    FileField,
    TextChoices,
    TextField,
)

from common.models import DjangoBaseModel


class NoticePublishedForChoice(TextChoices):
    ALL = "all", "All"
    TEACHER = "teacher", "Teacher"
    STUDENT = "student", "Student"


class PublishedStatusChoice(TextChoices):
    PUBLISHED = "published", "Published"
    DRAFT = "draft", "Draft"
    ARCHIVED = "archived", "Archived"


class Notice(DjangoBaseModel):
    title = CharField(
        max_length=255,
    )
    description = TextField(blank=True, null=True)
    file = FileField(
        upload_to="notices/",
        null=True,
        blank=True,
    )
    published_status = CharField(
        max_length=15,
        choices=PublishedStatusChoice.choices,
        default=PublishedStatusChoice.PUBLISHED,
    )
    published_for = CharField(
        max_length=10,
        choices=NoticePublishedForChoice.choices,
        default=NoticePublishedForChoice.ALL,
    )

    def __str__(self):
        return self.title
