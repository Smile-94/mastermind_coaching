from django.contrib.auth.mixins import UserPassesTestMixin
from common.models import UserTypeChoice


class TeacherPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == UserTypeChoice.TEACHER
