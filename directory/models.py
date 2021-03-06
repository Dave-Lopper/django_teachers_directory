from django.core.validators import RegexValidator
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(
        upload_to="directory/avatars",
        blank=True,
        default='directory/default-avatar.png')
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(
        max_length=16,
        validators=[RegexValidator(
            r'^\+\d{2,3}-\d{3}-\d{3}-\d{3}$',
            message="Phone number must be entered in the format: '+971-555-555-555'."  # noqa:E501
        )]
    )

    room = models.CharField(max_length=5)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
