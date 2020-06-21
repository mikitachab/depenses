from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from djmoney.money import Money
import pytest

from spendings.models import (
    Room,
    Member,
    Spending,
)


User = get_user_model()


def test_can_create_room():
    room = Room(name="room name", currency="USD")
    assert room.name == "room name"
    assert room.currency == "USD"


def test_can_create_member():
    user = User(username="testuser")
    room = Room(name="room name", currency="USD")

    member = Member(room=room, user=user)

    assert member.user.username == "testuser"
    assert member.room.name == "room name"


@pytest.mark.django_db
def test_cant_save_duplicate_member():
    user = User.objects.create(username="testuser")
    room = Room.objects.create(name="room name", currency="USD")
    Member.objects.create(room=room, user=user)

    with pytest.raises(IntegrityError) as e_info:
        Member.objects.create(room=room, user=user)
        assert "UNIQUE constraint failed" in str(e_info.value)


@pytest.mark.django_db
def test_can_create_room_with_2_members():
    user_1 = User.objects.create(username="user_1")
    user_2 = User.objects.create(username="user_2")
    room = Room.objects.create(name="room name", currency="USD")
    member_1 = Member.objects.create(room=room, user=user_1)
    member_2 = Member.objects.create(room=room, user=user_2)

    assert room.member_set.count() == 2
    assert member_1.room == member_2.room


def test_can_create_spending():
    user = User(username="testuser")
    room = Room(name="room name", currency="USD")
    member = Member(room=room, user=user)

    spending = Spending(member=member, title="some title", amount=Money(42, "USD"))

    assert spending.title == "some title"
    assert spending.member.room.name == "room name"
    assert spending.member.user.username == "testuser"
