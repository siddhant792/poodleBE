from django.urls import path

from apps.services import views as services_views


urlpatterns = [
    path('get-subjects', services_views.SubjectView.as_view(), name='get-subjects'),
    path('add-query', services_views.QueryView.as_view(), name='add-query'),
]
