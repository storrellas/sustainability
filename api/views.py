# Django importts
from django.shortcuts import render

# Dependencies
from rest_framework import viewsets

from .serializers import ConsumptionSerializer
from .models import Consumption

# Create your views here.
class ConsumptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
