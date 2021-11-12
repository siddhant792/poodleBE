from django.db import models


class Holders(models.Model):
    """
    Holders table for storing pre defined data (by admin user)
    """

    HOLDER_CHOICES = [
        ('SUBJECT', 'Subject'),
        ('UNIVERSITY', 'University'),
        ('STREAM', 'Stream'),
        ('COURSE', 'Course'),
    ]
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=100, null=False)
    type = models.CharField(choices=HOLDER_CHOICES, max_length=50)


class Query(models.Model):
    """
    Query of users
    """

    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    query = models.CharField(max_length=500, null=False)
