from rest_framework.routers import SimpleRouter

from django.urls import path

from apps.documents import views as document_views

router = SimpleRouter(trailing_slash=False)

router.register('upload',document_views.DocumentView, basename="upload")

urlpatterns = router.urls