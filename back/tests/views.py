"""
define views
"""
from django.shortcuts import render
from rest_framework import viewsets
from tests.serializers import TestsSerializer
from tests.models import Tests


class TestsView(viewsets.ModelViewSet):

    serializer_class = TestsSerializer
    queryset = Tests.objects.all()
