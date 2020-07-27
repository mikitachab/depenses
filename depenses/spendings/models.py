from django.conf import settings
from django.db import models
from django.db.models import Q, F
from djmoney.models.fields import MoneyField


class Room(models.Model):
    name = models.CharField(max_length=50)
    currency = models.CharField(max_length=3, choices=settings.CURRENCY_CHOICES)


class Member(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, default="")

    class Meta:
        unique_together = ("room", "name")


class Spending(models.Model):
    title = models.CharField(max_length=100)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class Dept(models.Model):
    title = models.CharField(max_length=100)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    from_member = models.ForeignKey("Member", on_delete=models.CASCADE, related_name="depts_from")
    to_member = models.ForeignKey("Member", on_delete=models.CASCADE, related_name="depts_to")
    date = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~Q(from_member_id=F("to_member_id")), name="not_from_to_same_member")
        ]


class Settlement(models.Model):
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    settlement_with_member = models.ForeignKey("Member", on_delete=models.CASCADE, related_name="settlements_with")
    date = models.DateTimeField(auto_now=True)
