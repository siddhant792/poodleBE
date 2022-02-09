from django.contrib import admin
from apps.documents import models as document_models


@admin.register(document_models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "subject",)
