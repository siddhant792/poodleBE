from rest_framework import generics as rest_framwork_generics

from apps.services import (
    models as services_models,
    serializers as services_serializers
)


class HoldersView(rest_framwork_generics.ListAPIView):
    """
    Fetch Holders View
    """
    serializer_class = services_serializers.HolderSerializer
    queryset = services_models.Holders.objects.all()


class QueryView(rest_framwork_generics.CreateAPIView):
    """
    Fetch Holders View
    """
    serializer_class = services_serializers.QuerySerializer