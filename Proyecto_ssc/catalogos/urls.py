from django.db import router
from rest_framework import routers
from .viewsets import SituacionViewSets, LenguajeDbViewSets, LenguajesViewSets

router = routers.SimpleRouter()
router.register('lenguajes', LenguajesViewSets)
router.register('situacion', SituacionViewSets)
router.register('lenguajedb', LenguajeDbViewSets)

urlpatterns = router.urls