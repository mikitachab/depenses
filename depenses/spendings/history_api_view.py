from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from spendings.member_check import check_room_member
from spendings import serializers
from spendings import models


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def room_history(request, room_id):
    room = get_object_or_404(models.Room, pk=room_id)
    check_room_member(request.user, room)

    depts = list(room.dept_set.all())
    spendings = list(room.spending_set.all())
    settlements = list(room.settlement_set.all())

    history = sorted(depts + spendings + settlements, key=lambda x: x.date, reverse=True)

    return Response(serialize_history(history))


def serialize_history(history):
    return [serialize_history_item(item) for item in history]


def serialize_history_item(item):
    data = {}
    if isinstance(item, models.Dept):
        data = serializers.DeptSerializer(item).data
        data["type"] = "dept"
    if isinstance(item, models.Spending):
        data = serializers.SpengingSerializer(item).data
        data["type"] = "spending"
    if isinstance(item, models.Settlement):
        data = serializers.SettlementSerializer(item).data
        data["type"] = "settlement"
    return data
