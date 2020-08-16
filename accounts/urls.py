from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

router.register('customer',CustomerViewSet,basename="customer")
router.register('fieldowner',FieldOwnerViewSet,basename="field_owner")
router.register('referee',RefereeViewSet,basename="referee")
path('rest-auth/', include('rest_auth.urls')),
path('rest-auth/registration/', include('rest_auth.registration.urls'))

urlpatterns = [
path('', include(router.urls)),
]