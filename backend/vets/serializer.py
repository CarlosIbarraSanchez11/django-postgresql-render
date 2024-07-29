from rest_framework import serializers
from .models import Vet

class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = '__all__'