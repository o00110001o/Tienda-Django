from rest_framework import serializers
from app.models import Planta

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
          model = Planta
          fields = '__all__'