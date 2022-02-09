from rest_framework import serializers as rest_framework_serializers

from apps.services import models as services_models


class SubjectSerializer(rest_framework_serializers.ModelSerializer):
    """
    Get all holders from db
    """
    class Meta:
        model = services_models.Subject
        fields = '__all__'


class QuerySerializer(rest_framework_serializers.ModelSerializer):
    """
    Get all holders from db
    """
    class Meta:
        model = services_models.Query
        fields = '__all__'
