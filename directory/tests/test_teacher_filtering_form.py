from django.test import TestCase
from django.urls import reverse

from ..models import Subject, Teacher


class TeacherFilteringFormTests(TestCase):
    def test_first_name_first_letter_filtering(self):
        """
        First name first char filtering works.
        """
        Teacher.objects.create(first_name="Dave", last_name="Lopper")
        Teacher.objects.create(
            first_name="Dudley",
            last_name="Strauss",
            email="unique@emdadil.com")
        response = self.client.post(
            reverse('directory:index'),
            {"first_name": "d", "last_name": "all", "subject": "0"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dudley Strauss")
        self.assertContains(response, "Dave Lopper")
        self.assertEqual(len(response.context['teachers']), 2)

    def test_last_name_first_letter_filtering(self):
        """
        Last name first char filtering works.
        """
        Teacher.objects.create(first_name="Dave", last_name="Lopper")
        Teacher.objects.create(
            first_name="Dudley",
            last_name="Strauss",
            email="unique@emdail.com")
        response = self.client.post(
            reverse('directory:index'),
            {"first_name": "d", "last_name": "s", "subject": "0"}
        )
        self.assertContains(response, "Dudley Strauss")
        self.assertNotContains(response, "Dave Lopper")
        self.assertEqual(len(response.context['teachers']), 1)

    def test_subjects_taught_filtering(
            self):
        """
        Last name first char filtering works.
        """
        chemistery = Subject.objects.create(name="Chemistery")
        physics = Subject.objects.create(name="Physics")
        dave = Teacher.objects.create(first_name="Dave", last_name="Lopper")
        dave.subjects.add(chemistery)
        dudley = Teacher.objects.create(
            first_name="Dudley",
            last_name="Strauss",
            email="unique@esmdail.com")
        dudley.subjects.add(physics)
        dudley.subjects.add(chemistery)
        response = self.client.post(
            reverse('directory:index'),
            {
                "first_name": "all",
                "last_name": "all",
                "subject": f"{chemistery.id}"
            }
        )
        self.assertContains(response, "Dudley Strauss")
        self.assertContains(response, "Dave Lopper")
        self.assertEqual(len(response.context['teachers']), 2)

        response = self.client.post(
            reverse('directory:index'),
            {
                "first_name": "all",
                "last_name": "all",
                "subject": f"{physics.id}"
            }
        )
        self.assertContains(response, "Dudley Strauss")
