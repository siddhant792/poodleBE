from django.contrib import admin
from apps.services import models as services_models


@admin.register(services_models.Holders)
class HolderAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


@admin.register(services_models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
