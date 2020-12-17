from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from spendings import serializers, models


class UserRoomsViewSet(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [
        JSONParser,
        FormParser,
        MultiPartParser
    ]
    serializer_class = serializers.RoomSerializer
    queryset = models.Room.objects.all()

    def get(self, request, *args, **kwargs):
        return Response([serializers.RoomSerializer(m.room).data for m in request.user.member_set.all()])

    def post(self, request, *args, **kwargs):
        room = serializers.RoomSerializer(data=request.data)
        if room.is_valid(raise_exception=True):
            created_room = room.save()
            user = request.user
            models.Member.objects.create(room=created_room, user=user, name=user.username)
            return Response(room.data)
