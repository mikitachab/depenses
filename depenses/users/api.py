from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from spendings import serializers, models


class UserRoomsViewSet(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self, request, *args, **kwargs):
        rooms = [m.room for m in request.user.member_set.all()]
        return Response([serializers.RoomSerializer(room).data for room in rooms])

    def post(self, request, *args, **kwargs):
        room = serializers.RoomSerializer(data=request.data)
        if room.is_valid(raise_exception=True):
            created_room = room.save()
            user = request.user
            models.Member.objects.create(room=created_room, user=user, name=user.username)
            return Response(room.data)
