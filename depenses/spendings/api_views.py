from rest_framework import viewsets

from spendings import models
from spendings import serializers


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
