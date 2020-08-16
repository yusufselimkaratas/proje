from django.urls import path, include

from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('address',AddressViewSet,basename="address")
router.register('field',FieldViewSet,basename="field")
router.register('field_conf',FieldConfigurationViewSet,basename="field_configuration")
router.register('field_dis',FieldOwnerDiscountViewSet,basename="field_discount")
router.register('agenda',AgendaViewSet,basename="agenda")
router.register('reservation',ReservationViewSet,basename="reservation")
router.register('comment',CommentViewSet,basename="comment")
router.register('team',TeamViewSet,basename="team")
router.register('match',MatchViewSet,basename="match")
router.register('goal',GoalViewSet,basename="goal")
router.register('playersearch',PlayerSearchViewSet,basename="playersearch")

urlpatterns = [
path('', include(router.urls)),


]