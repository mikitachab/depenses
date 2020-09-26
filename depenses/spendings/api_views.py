from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from spendings import models
from spendings import serializers
from spendings.services import RoomStateService


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer


class SpendingViewSet(viewsets.ModelViewSet):
    queryset = models.Spending.objects.all()
    serializer_class = serializers.SpengingSerializer


class DeptViewSet(viewsets.ModelViewSet):
    queryset = models.Dept.objects.all()
    serializer_class = serializers.DeptSerializer


class SettlementViewSet(viewsets.ModelViewSet):
    queryset = models.Settlement.objects.all()
    serializer_class = serializers.SettlementSerializer


@api_view()
def room_state(request, room_id):
    room = models.Room.objects.filter(id=room_id).first()

    room_state_service = RoomStateService(room)
    _room_state = room_state_service.calculate_room_state()
    return Response(_room_state.to_json())
