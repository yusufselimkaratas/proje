from rest_framework.authentication import TokenAuthentication

from .serializers import *
from rest_framework import viewsets
# Create your views here.

from rest_framework.permissions import IsAuthenticated
from proje.permissions import OwnerPermission
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import status
from datetime import datetime, timedelta, date


def int_to_bool(i, number):
    if i == 0:
        return bool(number & 0b000000000000000000000001)
    elif i == 1:
        return bool(number & 0b000000000000000000000010)
    elif i == 2:
        return bool(number & 0b000000000000000000000100)
    elif i == 3:
        return bool(number & 0b000000000000000000001000)
    elif i == 4:
        return bool(number & 0b000000000000000000010000)
    elif i == 5:
        return bool(number & 0b000000000000000000100000)
    elif i == 6:
        return bool(number & 0b000000000000000001000000)
    elif i == 7:
        return bool(number & 0b000000000000000010000000)
    elif i == 8:
        return bool(number & 0b000000000000000100000000)
    elif i == 9:
        return bool(number & 0b000000000000001000000000)
    elif i == 10:
        return bool(number & 0b000000000000010000000000)
    elif i == 11:
        return bool(number & 0b000000000000100000000000)
    elif i == 12:
        return bool(number & 0b000000000001000000000000)
    elif i == 13:
        return bool(number & 0b000000000010000000000000)
    elif i == 14:
        return bool(number & 0b000000000100000000000000)
    elif i == 15:
        return bool(number & 0b000000001000000000000000)
    elif i == 16:
        return bool(number & 0b000000010000000000000000)
    elif i == 17:
        return bool(number & 0b000000100000000000000000)
    elif i == 18:
        return bool(number & 0b000001000000000000000000)
    elif i == 19:
        return bool(number & 0b000010000000000000000000)
    elif i == 20:
        return bool(number & 0b000100000000000000000000)
    elif i == 21:
        return bool(number & 0b001000000000000000000000)
    elif i == 22:
        return bool(number & 0b010000000000000000000000)
    elif i == 23:
        return bool(number & 0b100000000000000000000000)
    else:
        return "ERROR"


class AddressViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)

    def get_serializer_class(self):
        if self.action in ['create']:
            return AddressCreateSerializer

        else:
            return AddressSerializer

    def get_queryset(self):
        if self.action in ['create']:
            pass
        elif self.action in ['own']:
            return Address.objects.filter(user_id=self.request.user.id)
        elif self.action in ['by_city']:
            city = self.request.data['city']
            return Address.objects.filter(city__icontains=city)

        else:
            return Address.objects.all()

    def get_permissions(self):
        # Your logic should be all here
        if self.request.method in ['DELETE', 'PUT', 'PATCH', 'UPDATE']:
            self.permission_classes = (OwnerPermission,)
        else:
            self.permission_classes = (IsAuthenticated,)

        return super(AddressViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['GET'])
    def own(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def by_city(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)


# TODO: Add method to check priority of address

class FieldViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        if self.action in ['create']:
            pass
        elif self.action in ['own']:
            return Field.objects.filter(owner__user_id=self.request.user.id)
        elif self.action in ['by_city']:
            city = self.request.data['city']
            return Field.objects.filter(address__city__icontains=city)

        else:
            return Field.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return FieldCreateSerializer
        else:
            return FieldsSerializer

    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT', 'PATCH', 'UPDATE']:
            self.permission_classes = (OwnerPermission,)
        else:
            self.permission_classes = (IsAuthenticated,)

        return super(FieldViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)

        address_id = serializer.validated_data['address'].id

        if Address.objects.filter(pk=address_id).count() < 1:
            return Response({'Error': 'No such Address'}, status=status.HTTP_401_UNAUTHORIZED)
        elif Address.objects.get(pk=address_id).user.id is not self.request.user.id:
            return Response({'Error': 'Wrong Address'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer.save(owner=FieldOwner.objects.get(user_id=self.request.user.id))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['GET'])
    def own(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def by_city(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)


class FieldConfigurationViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):

        if self.action in ['own']:
            return FieldConfiguration.objects.filter(field__owner__user_id=self.request.user.id)
        else:
            return FieldConfiguration.objects.all()

    def get_serializer_class(self):
        return FieldConfigurationSerializer

    def get_permissions(self):
        if self.request.method in ['DELETE', ]:
            self.permission_classes = (OwnerPermission,)
        else:
            self.permission_classes = (IsAuthenticated,)

        return super(FieldConfigurationViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)

        field_id = serializer.validated_data['field'].id

        if Field.objects.filter(pk=field_id).count() < 1:
            return Response({'Error': 'No such Field'}, status=status.HTTP_401_UNAUTHORIZED)
        elif Field.objects.get(pk=field_id).owner.user.id is not self.request.user.id:
            return Response({'Error': 'Wrong Field'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['GET'])
    def own(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)


class FieldOwnerDiscountViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):

        if self.action in ['own']:
            return FieldOwnerDiscount.objects.filter(field__owner__user_id=self.request.user.id)
        else:
            return FieldOwnerDiscount.objects.all()

    def get_serializer_class(self):
        return FieldOwnerDiscountSerializer

    def get_permissions(self):
        if self.request.method in ['DELETE', ]:
            self.permission_classes = (OwnerPermission,)
        else:
            self.permission_classes = (IsAuthenticated,)

        return super(FieldOwnerDiscountViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)

        field_id = serializer.validated_data['field'].id

        if Field.objects.filter(pk=field_id).count() < 1:
            return Response({'Error': 'No such Field'}, status=status.HTTP_401_UNAUTHORIZED)
        elif Field.objects.get(pk=field_id).owner.user.id is not self.request.user.id:
            return Response({'Error': 'Wrong Field'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['GET'])
    def own(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)


class AgendaViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):

        if self.action in ['own']:
            return Agenda.objects.filter(field__owner__user_id=self.request.user.id)
        else:
            return Agenda.objects.all()

    def get_serializer_class(self):
        return AgendaSerializer

    def get_permissions(self):

        self.permission_classes = (IsAuthenticated,)

        return super(AgendaViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)

        # DATE CHECK

        date_req = serializer.validated_data['date']
        field_id = serializer.validated_data['field'].id

        next_date = FieldConfiguration.objects.get(field_id=field_id).agenda_creation_day

        if date_req <= date.today():
            return Response({'Error': 'Wrong Date'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif (date_req - date.today()).days > next_date:
            return Response({'Error': 'Too Late'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            pass

        # AGENDA CHECK

        if Agenda.objects.filter(field_id=field_id, date=date_req).count() > 0:
            return Response({'Error': 'Already Have an Agenda for that Date'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            pass

        # FIELD-OWNER CHECK
        if Field.objects.filter(pk=field_id).count() < 1:
            return Response({'Error': 'No such Field'}, status=status.HTTP_401_UNAUTHORIZED)
        elif Field.objects.get(pk=field_id).owner.user.id is not self.request.user.id:
            return Response({'Error': 'Wrong Field'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            pass

        # DATA UNZIP

        field_obj = FieldConfiguration.objects.get(field_id=field_id)

        enable_zip = field_obj.enabled
        reserved_zip = field_obj.reserved_by_owner
        price_zip = field_obj.price

        active_0 = int_to_bool(0, enable_zip)
        active_1 = int_to_bool(1, enable_zip)
        active_2 = int_to_bool(2, enable_zip)
        active_3 = int_to_bool(3, enable_zip)
        active_4 = int_to_bool(4, enable_zip)
        active_5 = int_to_bool(5, enable_zip)
        active_6 = int_to_bool(6, enable_zip)
        active_7 = int_to_bool(7, enable_zip)
        active_8 = int_to_bool(8, enable_zip)
        active_9 = int_to_bool(9, enable_zip)
        active_10 = int_to_bool(10, enable_zip)
        active_11 = int_to_bool(11, enable_zip)
        active_12 = int_to_bool(12, enable_zip)
        active_13 = int_to_bool(13, enable_zip)
        active_14 = int_to_bool(14, enable_zip)
        active_15 = int_to_bool(15, enable_zip)
        active_16 = int_to_bool(16, enable_zip)
        active_17 = int_to_bool(17, enable_zip)
        active_18 = int_to_bool(18, enable_zip)
        active_19 = int_to_bool(19, enable_zip)
        active_20 = int_to_bool(20, enable_zip)
        active_21 = int_to_bool(21, enable_zip)
        active_22 = int_to_bool(22, enable_zip)
        active_23 = int_to_bool(23, enable_zip)

        reserved_0 = int_to_bool(0, reserved_zip)
        reserved_1 = int_to_bool(1, reserved_zip)
        reserved_2 = int_to_bool(2, reserved_zip)
        reserved_3 = int_to_bool(3, reserved_zip)
        reserved_4 = int_to_bool(4, reserved_zip)
        reserved_5 = int_to_bool(5, reserved_zip)
        reserved_6 = int_to_bool(6, reserved_zip)
        reserved_7 = int_to_bool(7, reserved_zip)
        reserved_8 = int_to_bool(8, reserved_zip)
        reserved_9 = int_to_bool(9, reserved_zip)
        reserved_10 = int_to_bool(10, reserved_zip)
        reserved_11 = int_to_bool(11, reserved_zip)
        reserved_12 = int_to_bool(12, reserved_zip)
        reserved_13 = int_to_bool(13, reserved_zip)
        reserved_14 = int_to_bool(14, reserved_zip)
        reserved_15 = int_to_bool(15, reserved_zip)
        reserved_16 = int_to_bool(16, reserved_zip)
        reserved_17 = int_to_bool(17, reserved_zip)
        reserved_18 = int_to_bool(18, reserved_zip)
        reserved_19 = int_to_bool(19, reserved_zip)
        reserved_20 = int_to_bool(20, reserved_zip)
        reserved_21 = int_to_bool(21, reserved_zip)
        reserved_22 = int_to_bool(22, reserved_zip)
        reserved_23 = int_to_bool(23, reserved_zip)

        serializer.save(active_0=active_0, active_1=active_1, active_2=active_2, active_3=active_3, active_4=active_4,
                        active_5=active_5, active_6=active_6, active_7=active_7, active_8=active_8, active_9=active_9,
                        active_10=active_10, active_11=active_11, active_12=active_12, active_13=active_13,
                        active_14=active_14, active_15=active_15, active_16=active_16, active_17=active_17,
                        active_18=active_18, active_19=active_19, active_20=active_20, active_21=active_21,
                        active_22=active_22, active_23=active_23, reserved_0=reserved_0, reserved_1=reserved_1,
                        reserved_2=reserved_2, reserved_3=reserved_3, reserved_4=reserved_4, reserved_5=reserved_5,
                        reserved_6=reserved_6, reserved_7=reserved_7, reserved_8=reserved_8, reserved_9=reserved_9,
                        reserved_10=reserved_10, reserved_11=reserved_11, reserved_12=reserved_12,
                        reserved_13=reserved_13, reserved_14=reserved_14, reserved_15=reserved_15,
                        reserved_16=reserved_16, reserved_17=reserved_17, reserved_18=reserved_18,
                        reserved_19=reserved_19, reserved_20=reserved_20, reserved_21=reserved_21,
                        reserved_22=reserved_22, reserved_23=reserved_23, price=price_zip)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class PlayerSearchViewSet(viewsets.ModelViewSet):
    queryset = PlayerSearch.objects.all()
    serializer_class = PlayerSearchSerializer