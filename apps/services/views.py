from rest_framework import generics as rest_framwork_generics
from rest_framework.permissions import AllowAny

from apps.services import (
    models as services_models,
    serializers as services_serializers
)


class SubjectView(rest_framwork_generics.ListAPIView):
    """
    Fetch Holders View
    """
    permission_classes = [AllowAny]
    serializer_class = services_serializers.SubjectSerializer
    queryset = services_models.Subject.objects.all()


class QueryView(rest_framwork_generics.CreateAPIView):
    """
    Fetch Holders View
    """
    serializer_class = services_serializers.QuerySerializer
    permission_classes = [AllowAny]
