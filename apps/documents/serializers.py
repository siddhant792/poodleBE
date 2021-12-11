from rest_framework import (
    serializers as rest_framework_serializers,
    validators as rest_framework_validators,
)

from apps.documents import (
    models as document_models,
    utils as document_utils,
)

from apps.documents import constants as document_constants

class DocumentSerializer(rest_framework_serializers.ModelSerializer):
    """
    Serializer for documents operation
    """
    file = rest_framework_serializers.FileField(write_only=True)

    class Meta:
        model = document_models.Document
        fields = ("name", "subject", "course", "semester", "university", "file")

    def validate_file(self, file):
        if file.size/1000000 > 50:
            raise rest_framework_validators.ValidationError("Please upload a document of maximum 50 mb")
        return file

    def create(self, validated_data):
        user=self.context['request'].user
        try:
            cloud_path = document_utils.upload_document(user, validated_data['name'], validated_data['file'])
            document = {
                'name': validated_data['name'],
                'subject': validated_data['subject'],
                'course': validated_data['course'],
                'semester': validated_data['semester'],
                'university': validated_data['university'],
                'author': user,
                'path': cloud_path
            }
        except:
            raise rest_framework_validators.ValidationError(document_constants.UPLOAD_ERROR_MSG)
        return super().create(document)
