from rest_framework import viewsets as rest_framwork_viewsets
from rest_framework import generics as rest_framwork_generics
from rest_framework.response import Response

from django.db.models import Value, F
from django.db.models.functions import Concat

from apps.documents import (
    serializers as document_serializers,
    models as document_models
)


class DocumentView(rest_framwork_viewsets.ModelViewSet):
    serializer_class = document_serializers.DocumentSerializer
    queryset = document_models.Document.objects.all()


class FetchDocumentView(rest_framwork_generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        subject_code = request.data.get('subject_code')
        all_docs = document_models.Document.objects.annotate(
            full_name=Concat('author__first_name', Value(' '), 'author__last_name')
        ).filter(subject=subject_code).values(
            'subject', 'course', 'semester', 'university',document_name=F('name'), document_url = F('path'), author_name=F('full_name')
        )
        return Response(all_docs)
