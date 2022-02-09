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
        service_models.Subject, help_text="Subject to which the document is related", on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        accounts_models.User, help_text="User info who is author of this document", on_delete=models.CASCADE
    )
    path = CharField(max_length=200, help_text="Path where the document is stored in cloud storage")
