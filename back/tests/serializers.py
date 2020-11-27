"""
define serializer
"""
from rest_framework import serializers
from tests.models import Tests


class TestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tests
        fields = (
            "name",
        )
