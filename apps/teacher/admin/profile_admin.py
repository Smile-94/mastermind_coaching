from django.contrib.admin import (
    ModelAdmin,
    # Methods
    register,
)

# Import All Model from model Directory
from apps.teacher.models.profile_model import (
    TeacherProfile,
    Address,
    EducationalQualification,
)


# * <<-----------------------*** Teacher Profile Admin *** ------------------------------>>
@register(TeacherProfile)
class TeacherProfileAdmin(ModelAdmin):
    """
    Admin interface for the Product Brand model.
    """

    list_display = (
        "id",
        "profile_of__username",
        "date_of_birth",
        "gender",
        "nationality",
        "marital_status",
    )
    list_editable = ("gender",)
    list_display_links = ("id",)
    search_fields = (
        "id",
        "profile_of__username",
        "profile_of__email",
        "profile_of__name",
    )
    list_filter = ("gender",)
    list_per_page = 50


# * <<--------------------------------------*** Teacher Address Admin ***---------------------------------->>
@register(Address)
class AddressAdmin(ModelAdmin):
    """
    Admin interface for teacher address.
    """

    list_display = (
        "id",
        "address_of",
        "address",
        "city",
        "state",
        "country",
        "zip_code",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "address_of__username",
        "address_of__email",
        "address_of__name",
    )
    list_per_page = 50


# * <<------------------------------------*** Teacher Educational Qualification Admin ***----------------------------->>
@register(EducationalQualification)
class EducationalQualificationAdmin(ModelAdmin):
    """
    Admin interface for teacher educational qualification.
    """

    list_display = (
        "id",
        "teacher",
        "degree",
        "institution",
        "passing_year",
        "grade_or_cgpa",
        "specialization",
        "achievements",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "address_of__username",
        "address_of__email",
        "address_of__name",
    )
    list_per_page = 50
