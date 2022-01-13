from django.db import models
from django.db.models.fields import CharField

from apps.accounts import models as accounts_models
from apps.services import models as service_models

class Document(models.Model):
    """
    Documents (Notes) uploaded by the user
    """
    name = models.CharField( max_length=50, help_text='Title of the document')
    subject = models.ForeignKey(
        service_models.Holder, help_text="Subject to which the document is related", on_delete=models.CASCADE, related_name='subject'
    )
    course = models.ForeignKey(
        service_models.Holder, help_text="Course to which the document is related", on_delete=models.CASCADE, related_name='course'
    )
    semester = models.ForeignKey(
        service_models.Holder, help_text="Semester to which the document is related", on_delete=models.CASCADE, related_name='semester'
    )
    university = models.ForeignKey(
        service_models.Holder, help_text="University to which the document is related", on_delete=models.CASCADE, related_name='university'
    )
    stream = models.ForeignKey(
        service_models.Holder, help_text="Stream to which the document is related", on_delete=models.CASCADE, related_name='stream'
    )
    author = models.ForeignKey(
        accounts_models.User, help_text="User info who is author of this document", on_delete=models.CASCADE
    )
    path = CharField(max_length=200, help_text="Path where the document is stored in cloud storage")
