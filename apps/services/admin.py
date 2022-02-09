from django.contrib import admin
from apps.services import models as services_models


@admin.register(services_models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields=('slug',)


@admin.register(services_models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields=('slug',)


@admin.register(services_models.Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields=('slug',)


@admin.register(services_models.Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("number", "slug")
    readonly_fields=('slug',)


@admin.register(services_models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields=('slug',)


@admin.register(services_models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
