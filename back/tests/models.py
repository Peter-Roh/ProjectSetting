"""
define models
"""
from django.db import models


class Tests(models.Model):
    """ tests model definition """
    name = models.CharField(max_length=50, null=True, blank=True)
