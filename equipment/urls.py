from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

router.register('crampon',CramponViewSet,basename="crampon")
router.register('short',ShortViewSet,basename="short")
router.register('shirt',ShirtViewSet,basename="shirt")
router.register('equipment',EquipmentViewSet,basename="equipment")

urlpatterns = [
    path('', include(router.urls)),
]