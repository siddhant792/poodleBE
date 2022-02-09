from rest_framework import (
    serializers as rest_framework_serializers,
    validators as rest_framework_validators,
)

from apps.documents import (
    models as document_models,
    utils as document_utils,
)

from apps.documents import constants as document_constants
from apps.services import models as service_models


class DocumentSerializer(rest_framework_serializers.ModelSerializer):
    """
    Serializer for documents operation
    """
    file = rest_framework_serializers.FileField(write_only=True)
    subject_slug = rest_framework_serializers.CharField()

    class Meta:
        model = document_models.Document
        fields = ("name", "subject_slug", "file")

    def validate_file(self, file):
        if file.size/1000000 > 50:
            raise rest_framework_validators.ValidationError("Please upload a document of maximum 50 mb")
        return file

    def to_representation(self, instance):
        return {
            'name': instance.name,
            'subject': instance.subject.name,
            'course': instance.subject.stream.course.name,
            'semester': instance.subject.semester.number,
            'stream': instance.subject.stream.name,
            'university': instance.subject.stream.course.university.name,
            'author': instance.author.first_name + ' ' + instance.author.last_name,
            'path': instance.path,
        }

    def create(self, validated_data):
        user=self.context['request'].user
        subject = service_models.Subject.objects.filter(slug=validated_data['subject_slug']).first()
        try:
            cloud_path = document_utils.upload_document(user, validated_data['name'], validated_data['file'])
            document = {
                'name': validated_data['name'],
                'subject': subject,
                'author': user,
                'path': cloud_path
            }
        except:
            raise rest_framework_validators.ValidationError(document_constants.UPLOAD_ERROR_MSG)
        return super().create(document)
