from django.db import models


class Holder(models.Model):
    """
    Holders table for storing pre defined data (by admin user)
    """

    HOLDER_CHOICES = [
        ('SUBJECT', 'Subject'),
        ('UNIVERSITY', 'University'),
        ('STREAM', 'Stream'),
        ('COURSE', 'Course'),
        ('SEMESTER', 'Semester'),
    ]
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=100, null=False, unique=True)
    type = models.CharField(choices=HOLDER_CHOICES, max_length=50)

    def __str__(self) -> str:
        return self.name


class Query(models.Model):
    """
    Query of users
    """

    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    query = models.CharField(max_length=500, null=False)
