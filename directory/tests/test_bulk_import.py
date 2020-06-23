import csv
import os

from django.test import TestCase

from ..models import Subject, Teacher
from ..bulk_importer import bulk_insert


class BulkImportTests(TestCase):
    def test_bulk_import_inserts_subects(self):
        path = os.path.dirname(os.path.realpath(__file__))
        zip_file = os.path.join(
            path,
            "assets/",
            "archive.zip"
        )
        csv_file = open(os.path.join(
            path,
            "assets/",
            "sample.csv"
        ))

        csv_reader = csv.reader(csv_file, delimiter=',')
        return_value = bulk_insert(csv_reader, zip_file)
        self.assertEqual(return_value, 0)
        self.assertEqual(Subject.objects.count(), 3)
        self.assertIn("Physics", list(
            map(lambda x: x.name, Subject.objects.all())))
        self.assertIn("Computer science", list(
            map(lambda x: x.name, Subject.objects.all())))
        self.assertIn("Mathematics", list(
            map(lambda x: x.name, Subject.objects.all())))

    def test_bulk_import_inserts_valid_rows(self):
        """
        Bulk import inserts valid rows correctly
        """
        maths = Subject.objects.create(name="Mathematics")
        cs = Subject.objects.create(name="Computer science")
        physics = Subject.objects.create(name="Physics")
        path = os.path.dirname(os.path.realpath(__file__))

        zip_file = os.path.join(
            path,
            "assets/",
            "archive.zip"
        )
        csv_file = open(os.path.join(
            path,
            "assets/",
            "sample.csv"
        ))

        csv_reader = csv.reader(csv_file, delimiter=',')
        return_value = bulk_insert(csv_reader, zip_file)
        self.assertEqual(return_value, 0)
        self.assertEqual(Teacher.objects.count(), 2)
        self.assertTrue(
            Teacher.objects.filter(
                first_name="Dave").first() is not None
        )

        dave = Teacher.objects.filter(first_name="Dave").first()
        self.assertIn("mongo", dave.profile_picture.path)
        self.assertEqual(dave.last_name, "Lopper")
        self.assertEqual(dave.email, "dave-lopper@school.com")
        self.assertEqual(dave.phone, "+971-505-550-507")
        self.assertEqual(dave.room, "3a")
        self.assertIn(cs, dave.subjects.all())
        self.assertIn(physics, dave.subjects.all())

        dudley = Teacher.objects.filter(first_name="Dudley").first()
        self.assertIn("travis", dudley.profile_picture.path)
        self.assertEqual(dudley.last_name, "Strauss")
        self.assertEqual(dudley.email, "dudley-strauss@school.com")
        self.assertEqual(dudley.phone, "+971-585-554-431")
        self.assertEqual(dudley.room, "1c")
        self.assertIn(maths, dudley.subjects.all())
