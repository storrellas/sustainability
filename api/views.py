# Django importts
from django.shortcuts import render

# Dependencies
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

# Project
from .serializers import ConsumptionSerializer
from .models import Consumption

# Create your views here.
class ConsumptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
    renderer_classes = (JSONRenderer, )

# Create your views here.
class ConsumptionXMLViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
    renderer_classes = (XMLRenderer, )
