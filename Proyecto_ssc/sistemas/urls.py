from django.db import router
from rest_framework import routers
from .viewsets import SistemaViewSet

router = routers.SimpleRouter()
router.register('sistema', SistemaViewSet)

urlpatterns = router.urls