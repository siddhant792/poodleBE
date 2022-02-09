from django.db import models
from django.template.defaultfilters import slugify


class University(models.Model):
    """
    Holders table for storing pre defined data (by admin user)
    """
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(University, self).save(*args, **kwargs)


class Course(models.Model):
    """
    Holders table for storing pre defined data (by admin user)
    """
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)


class Stream(models.Model):
    """
    Holders table for storing pre defined data (by admin user)
    """
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Stream, self).save(*args, **kwargs)

class Semester(models.Model):
    """
    Holders table for storing pre defined data (by admin user)
    """
    number = models.CharField(max_length=100, null=False)
    slug = models.SlugField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.number

    def save(self, *args, **kwargs):
        self.slug = slugify(self.number)
        super(Semester, self).save(*args, **kwargs)


class Subject(models.Model):
    """
    Holders table for storing pre defined data (by admin user)
    """
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField()
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)


class Query(models.Model):
    """
    Query of users
    """

    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    query = models.CharField(max_length=500, null=False)
