from rest_framework import viewsets as rest_framwork_viewsets

from apps.documents import (
    serializers as document_serializers,
    models as document_models
)


class DocumentView(rest_framwork_viewsets.ModelViewSet):
    serializer_class = document_serializers.DocumentSerializer
    queryset = document_models.Document.objects.all()
