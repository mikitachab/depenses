from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from spendings import models
from spendings import serializers
from spendings.services import RoomStateService


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def room_depts(request, room_id):
    room = get_object_or_404(models.Room, pk=room_id)
    check_room_member(request.user, room)
    depts = room.dept_set.all()
    return Response([serializers.DeptSerializer(d).data for d in depts])


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def room_spendings(request, room_id):
    room = get_object_or_404(models.Room, pk=room_id)
    check_room_member(request.user, room)
    spendings = room.spending_set.all()
    return Response([serializers.SpengingSerializer(s).data for s in spendings])


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def room_settlements(request, room_id):
    room = get_object_or_404(models.Room, pk=room_id)
    check_room_member(request.user, room)
    spendings = room.settlement_set.all()
    return Response([serializers.SettlementSerializer(s).data for s in spendings])


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def room_members(request, room_id):
    room = get_object_or_404(models.Room, pk=room_id)
    check_room_member(request.user, room)
    spendings = room.member_set.all()
    return Response([serializers.MemberSerializer(s).data for s in spendings])


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def room_state(request, room_id):
    room = get_object_or_404(models.Room, pk=room_id)
    check_room_member(request.user, room)
    room_state_service = RoomStateService(room)
    _room_state = room_state_service.calculate_room_state()
    return Response(_room_state.to_json())


def check_room_member(user, room):
    room_members = room.member_set.all()
    user_members = user.member_set.all()

    if not set(room_members).intersection(set(user_members)):
        raise PermissionDenied
