from django.db import models
from rest_framework import fields, serializers
from .models import PropertyTypes

class PropertyTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyTypes
        fields = '__all__'