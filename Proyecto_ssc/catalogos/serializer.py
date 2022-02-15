from django.db.models import fields
from rest_framework import serializers
from .models import Situacion, Lenguajes, LenguajeDb


class SituacionSerial(serializers.ModelSerializer):
    class Meta:
        model = Situacion
        fields = '__all__'

class LenguajesSerial(serializers.ModelSerializer):
    class Meta:
        model = Lenguajes
        fields = '__all__'

class LenguajeDbSerial(serializers.ModelSerializer):
    class Meta:
        model = LenguajeDb
        fields = '__all__'        
        