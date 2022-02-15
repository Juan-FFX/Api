from rest_framework import serializers
from django.db.models import fields
from .models import Base


class BaseSerial(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'