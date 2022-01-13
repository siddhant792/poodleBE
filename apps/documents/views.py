from re import sub
from rest_framework import viewsets as rest_framwork_viewsets
from rest_framework import generics as rest_framwork_generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from django.db.models import Value, F
from django.db.models.functions import Concat

from apps.documents import (
    serializers as document_serializers,
    models as document_models
)
from apps.services import models as service_models


class DocumentView(rest_framwork_viewsets.ModelViewSet):
    serializer_class = document_serializers.DocumentSerializer
    queryset = document_models.Document.objects.all()


class FetchDocumentView(rest_framwork_generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    
    def retrieve(self, request, *args, **kwargs):
        subject =  service_models.Holder.objects.filter(code=request.data.get('subject_code'), type='SUBJECT').first()
        if not subject:
            return Response({'subject_code': "Not a valid subject"}, status=status.HTTP_404_NOT_FOUND)
        all_docs = document_models.Document.objects.annotate(
            full_name=Concat('author__first_name', Value(' '), 'author__last_name')
        ).filter(subject=subject).values(
            'subject', 'course', 'semester', 'university', document_name=F('name'), document_url = F('path'), author_name=F('full_name')
        )
        return Response({
            "subject_name": subject.name,
            "documents": all_docs
        })
