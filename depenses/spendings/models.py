from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q, F
from djmoney.models.fields import MoneyField


class Room(models.Model):
    name = models.CharField(max_length=50)
    currency = models.CharField(max_length=3, choices=settings.CURRENCY_CHOICES)

    def __str__(self):
        return self.name

    def get_last_settlement(self):
        return self.settlement_set.order_by("-date").first()

    def get_spendings_after(self, date):
        return self.spending_set.filter(date__gt=date).all() if date else self.spending_set.all()

    def get_depts_after(self, date):
        return self.dept_set.filter(date__gt=date).all() if date else self.dept_set.all()


class Member(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + str(self.room)

    def clean(self):
        if self.name == "":
            raise ValidationError("member name can't be empty")

    class Meta:
        unique_together = [("room", "user"), ("room", "name")]


class Spending(models.Model):
    title = models.CharField(max_length=100)
    room = models.ForeignKey("Room", on_delete=models.CASCADE, null=False)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.member not in self.room.member_set.all():
            raise ValidationError("member is not part of a room")
        self.amount_currency = self.room.currency

    def __str__(self):
        return self.title


class Dept(models.Model):
    title = models.CharField(max_length=100)
    room = models.ForeignKey("Room", on_delete=models.CASCADE, null=False)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    from_member = models.ForeignKey("Member", on_delete=models.CASCADE, related_name="depts_from")
    to_member = models.ForeignKey("Member", on_delete=models.CASCADE, related_name="depts_to")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.from_member not in self.room.member_set.all():
            raise ValidationError("from_member is not part of a room")
        if self.to_member not in self.room.member_set.all():
            raise ValidationError("to_member is not part of a room")

        self.amount_currency = self.room.currency

    class Meta:
        constraints = [
            models.CheckConstraint(check=~Q(from_member_id=F("to_member_id")), name="not_from_to_same_member")
        ]


class Settlement(models.Model):
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    settlement_with_member = models.ForeignKey("Member", on_delete=models.CASCADE, related_name="settlements_with")
    room = models.ForeignKey("Room", on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.member)

    def clean(self):
        if self.member == self.settlement_with_member:
            raise ValidationError("Can't settlement with same member")
        if self.member not in self.room.member_set.all():
            raise ValidationError("member is not part of a room")
        if self.settlement_with_member not in self.room.member_set.all():
            raise ValidationError("settlement_with_member is not part of a room")

    class Meta:
        constraints = [
            models.CheckConstraint(check=~Q(member_id=F("settlement_with_member_id")), name="not_with_same_member")
        ]
