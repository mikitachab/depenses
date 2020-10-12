from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from spendings import models
from spendings import serializers
from spendings.services import RoomStateService


@api_view()
def room_depts(request, room_id):
    room = get_object_or_404(models.Room, pk=room_id)
    depts = room.dept_set.all()
    return Response([serializers.DeptSerializer(d).data for d in depts])


@api_view()
def room_spendings(reuqest, room_id):
    room = get_object_or_404(models.Room, pk=room_id)
    spendings = room.spending_set.all()
    return Response([serializers.SpengingSerializer(s).data for s in spendings])


@api_view()
def room_state(request, room_id):
    room = get_object_or_404(models.Room, pk=room_id)

    room_state_service = RoomStateService(room)
    _room_state = room_state_service.calculate_room_state()
    return Response(_room_state.to_json())
