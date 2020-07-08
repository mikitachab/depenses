from rest_framework import serializers

from spendings import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = "__all__"


class SpengingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spending
        fields = "__all__"


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dept
        fields = "__all__"


class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settlement
        fields = "__all__"
