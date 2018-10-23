# Dependencies
from rest_framework import serializers

# Project imports
from .models import Consumption

class ConsumptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consumption
        fields = '__all__'
