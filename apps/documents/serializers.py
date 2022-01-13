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
    subject_code = rest_framework_serializers.CharField()
    course_code = rest_framework_serializers.CharField()
    semester_code = rest_framework_serializers.CharField()
    university_code = rest_framework_serializers.CharField()
    stream_code = rest_framework_serializers.CharField()

    class Meta:
        model = document_models.Document
        fields = ("name", "subject_code", "course_code", "semester_code", "university_code", "stream_code", "file")

    def validate_file(self, file):
        if file.size/1000000 > 50:
            raise rest_framework_validators.ValidationError("Please upload a document of maximum 50 mb")
        return file

    def to_representation(self, instance):
        return {
            'name': instance.name,
            'subject': instance.subject.name,
            'course': instance.course.name,
            'semester': instance.semester.name,
            'stream': instance.stream.name,
            'university': instance.university.name,
            'author': instance.author.first_name + ' ' + instance.author.last_name,
            'path': instance.path,
        }

    def create(self, validated_data):
        user=self.context['request'].user
        subject = service_models.Holder.objects.filter(code=validated_data['subject_code'], type='SUBJECT').first()
        course = service_models.Holder.objects.filter(code=validated_data['course_code'], type='COURSE').first()
        semester = service_models.Holder.objects.filter(code=validated_data['semester_code'], type='SEMESTER').first()
        stream = service_models.Holder.objects.filter(code=validated_data['stream_code'],type='STREAM').first()
        university = service_models.Holder.objects.filter(code=validated_data['university_code'],type='UNIVERSITY').first()

        print(subject)
        try:
            cloud_path = document_utils.upload_document(user, validated_data['name'], validated_data['file'])
            document = {
                'name': validated_data['name'],
                'subject': subject,
                'course': course,
                'semester': semester,
                'stream': stream,
                'university': university,
                'author': user,
                'path': cloud_path
            }
        except:
            raise rest_framework_validators.ValidationError(document_constants.UPLOAD_ERROR_MSG)
        return super().create(document)
