from django.contrib import admin
from apps.accounts import models as accounts_models


@admin.register(accounts_models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
