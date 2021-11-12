from django.urls import path

from apps.services import views as services_views


urlpatterns = [
    path('getHolders', services_views.HoldersView.as_view(), name='get-holders'),
    path('addQuery', services_views.QueryView.as_view(), name='add-query'),
]
