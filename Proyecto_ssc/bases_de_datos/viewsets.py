from rest_framework import viewsets
from .models import Base
from .serializer import BaseSerial


class BaseViewSet(viewsets.ModelViewSet):
    queryset = Base.objects.all()
    serializer_class = BaseSerial