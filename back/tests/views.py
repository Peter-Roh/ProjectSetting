"""
define views
"""
from django.shortcuts import render
from rest_framework import viewsets
from tests.models import Tests
from tests.serializers import TestsSerializer


class TestsView(viewsets.ModelViewSet):

    serializer_class = TestsSerializer
    queryset = Tests.objects.all()
