from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField


class Room(models.Model):
    name = models.CharField(max_length=50)
    currency = models.CharField(max_length=3, choices=settings.CURRENCY_CHOICES)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Member")

    def __str__(self):
        return f"{self.name} {self.currency}"


class Member(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    joined = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("room", "user")

    def __str__(self):
        return f"{self.user.username} - {self.room.name}"


class Spending(models.Model):
    title = models.CharField(max_length=100)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    member = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.member.user.username} - {self.member.room.name} - {self.title} - {self.amount}"
