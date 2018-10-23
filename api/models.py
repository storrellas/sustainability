from django.db import models



class Consumption(models.Model):
    organization_id = models.IntegerField(null=True)
    organization = models.CharField(max_length=500,null=True)
    kpi = models.CharField(max_length=500,null=True)
    kpi_sub = models.CharField(max_length=500,null=True)
    value = models.IntegerField(null=True)
    comments = models.CharField(max_length=500,null=True)
    unit = models.CharField(max_length=500,null=True)
    date = models.CharField(max_length=500,null=True)
    period = models.CharField(max_length=500,null=True)
