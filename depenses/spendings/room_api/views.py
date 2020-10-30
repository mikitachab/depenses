from django.http import HttpResponseServerError

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from spendings import serializers, models
from spendings.services import RoomStateService, RoomHistoryService
from spendings.room_api.room_endpoint import room_endpoint


@room_endpoint(["GET"], [IsAuthenticated])
def room_depts(request, room):
    depts = room.dept_set.all()
    return Response([serializers.DeptSerializer(d).data for d in depts])


@room_endpoint(["GET"], [IsAuthenticated])
def room_spendings(request, room):
    spendings = room.spending_set.all()
    return Response([serializers.SpengingSerializer(s).data for s in spendings])


@room_endpoint(["GET"], [IsAuthenticated])
def room_settlements(request, room):
    spendings = room.settlement_set.all()
    return Response([serializers.SettlementSerializer(s).data for s in spendings])


@room_endpoint(["GET"], [IsAuthenticated])
def room_members(request, room):
    members = room.member_set.all()
    return Response([serializers.MemberSerializer(s).data for s in members])


@room_endpoint(["GET"], [IsAuthenticated])
def room_state(request, room):
    room_state_service = RoomStateService(room)
    _room_state = room_state_service.calculate_room_state()
    return Response(_room_state.to_json())


@room_endpoint(["GET"], [IsAuthenticated])
def room_history(request, room):
    room_history_service = RoomHistoryService(room)
    _room_history = room_history_service.get_history()
    return Response(_room_history.to_json())


@room_endpoint(["GET"], [IsAuthenticated])
def room_member(request, room):
    member = models.Member.objects.filter(user=request.user, room=room).first()
    if not member:
        return HttpResponseServerError()
    data = serializers.MemberSerializer(member).data
    data["user"] = {"username": request.user.username}
    return Response(data)


@room_endpoint(["GET"], [IsAuthenticated])
def room_data(request, room):
    member = models.Member.objects.filter(user=request.user, room=room).first()
    if not member:
        return HttpResponseServerError()
    member_data = serializers.MemberSerializer(member).data
    member_data["user"] = {"username": request.user.username}

    room_state_service = RoomStateService(room)
    _room_state = room_state_service.calculate_room_state()
    room_history_service = RoomHistoryService(room)
    _room_history = room_history_service.get_history()
    data = {
        "history": _room_history.to_json(),
        "members": [serializers.MemberSerializer(m).data for m in room.member_set.all()],
        "state": _room_state.to_json(),
        "current_user": member_data,
    }
    return Response(data)
