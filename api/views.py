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
    retrieve:
        Return a single item of Consumption

    list:
        Return a list of Consumption

    create:
        Creates a Consumption model

    destroy:
        Delete a Consumption model

    update:
        Update a Consumption model

    partial_update:
        Update a Consumption model
    """

    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
    renderer_classes = (JSONRenderer, )

# Create your views here.
class ConsumptionXMLViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a single item of Consumption in XML

    list:
        Return a list of Consumption in XML

    create:
        Creates a Consumption model in XML

    destroy:
        Delete a Consumption model in XML

    update:
        Update a Consumption model in XML

    partial_update:
        Update a Consumption model in XML
    """
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
    renderer_classes = (XMLRenderer, )
