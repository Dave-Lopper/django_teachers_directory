from django.test import TestCase

from ..models import Teacher


class TeacherModelTest(TestCase):

    def test_pp_has_its_default_value(self):
        """
        profile_picture has expected default value when not provided.
        """
        teacher = Teacher.objects.create(
            first_name="Dave",
            last_name="Lopper",
            phone="+971-555-555-555",
            room="95C"
        )
        self.assertEqual(
            teacher.profile_picture,
            'directory/default-avatar.png'
        )
