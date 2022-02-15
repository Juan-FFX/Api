from rest_framework import serializers
from .models import Sistema

class SistemaSerial(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = '__all__'
        

        