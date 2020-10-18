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
    member_name = serializers.CharField(source="member.name", read_only=True)

    class Meta:
        model = models.Spending
        fields = "__all__"

    def validate(self, attrs):
        instance = models.Spending(**attrs)
        instance.full_clean()
        return attrs


class DeptSerializer(serializers.ModelSerializer):
    from_member_name = serializers.CharField(source="from_member.name", read_only=True)
    to_member_name = serializers.CharField(source="to_member.name", read_only=True)

    class Meta:
        model = models.Dept
        fields = "__all__"

    def validate(self, attrs):
        if attrs["from_member"] == attrs["to_member"]:
            raise serializers.ValidationError("debt cannot be from and to the same member")
        instance = models.Dept(**attrs)
        instance.full_clean()
        return attrs


class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settlement
        fields = "__all__"

    def validate(self, attrs):
        instance = models.Settlement(**attrs)
        instance.full_clean()
        return attrs
