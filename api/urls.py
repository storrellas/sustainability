from rest_framework import routers
from .views import ConsumptionViewSet
from django.conf.urls import url,include


router = routers.DefaultRouter()
router.register(r'consumption', ConsumptionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
