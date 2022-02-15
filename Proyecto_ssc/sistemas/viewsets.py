from rest_framework import viewsets
from .models import Sistema
from .serializer import SistemaSerial

class SistemaViewSet(viewsets.ModelViewSet):
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerial
    