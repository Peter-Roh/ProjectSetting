"""
define api urls
"""
from django.urls import include
from django.urls import path
from rest_framework import routers
from tests import views as test_views


app_name = "apis"


router = routers.DefaultRouter()

router.register(r'test', test_views.TestsView, 'test')

urlpatterns = [
    path("", include(router.urls)),
]
