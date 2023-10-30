from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import apps
from .views import NetworkNodeViewSet

app_name = apps.NetworkConfig.name

router = DefaultRouter()
router.register(r'network-nodes', NetworkNodeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]