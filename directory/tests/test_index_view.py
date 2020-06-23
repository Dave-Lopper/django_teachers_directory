from django.test import TestCase
from django.urls import reverse

from ..models import Teacher


class IndexViewTests(TestCase):
    def test_no_teacher(self):
        """
        If no teacher exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('directory:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Oops, looks like no teacher matching your criteria have been added yet !")  # noqa:E501
        self.assertQuerysetEqual(response.context['teachers'], [])

    def test_past_question(self):
        """
        Inserted teachers are displayed on index page.
        """
        Teacher.objects.create(first_name="Dave", last_name="Lopper")
        response = self.client.get(reverse('directory:index'))
        self.assertContains(response, "Dave Lopper")
        self.assertQuerysetEqual(
            response.context['teachers'],
            ['<Teacher: Dave\xa0Lopper>']
        )
