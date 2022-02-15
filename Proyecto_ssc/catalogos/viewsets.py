from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Situacion, Lenguajes, LenguajeDb
from .serializer import SituacionSerial, LenguajesSerial, LenguajeDbSerial


class SituacionViewSets(viewsets.ModelViewSet):
    queryset = Situacion.objects.all()
    serializer_class = SituacionSerial
    http_method_names = ['get']

class LenguajesViewSets(viewsets.ModelViewSet):
    queryset = Lenguajes.objects.all()
    serializer_class = LenguajesSerial
    http_method_names = ['get']
    
class LenguajeDbViewSets(viewsets.ModelViewSet):
    queryset = LenguajeDb.objects.all()
    serializer_class = LenguajeDbSerial
    http_method_names = ['get']