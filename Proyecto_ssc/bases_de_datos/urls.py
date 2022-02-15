from django.db import router
from rest_framework import routers
from .viewsets import BaseViewSet


router = routers.SimpleRouter()
router.register('bases', BaseViewSet)

urlpatterns = router.urls