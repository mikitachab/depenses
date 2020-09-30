from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from djmoney.money import Money
import pytest

from spendings.models import (
    Room,
    Member,
    Spending,
    Dept,
    Settlement,
)


def test_can_create_room():
    room = Room(name="room name", currency="USD")
    assert room.name == "room name"
    assert room.currency == "USD"


@pytest.mark.django_db
def test_cant_save_duplicate_member():
    room = Room.objects.create(name="room name", currency="USD")
    user = get_user_model().objects.create(username="testuser")
    Member.objects.create(room=room, user=user)

    with pytest.raises(IntegrityError) as e_info:
        Member.objects.create(room=room, user=user)
        assert "UNIQUE constraint failed" in str(e_info.value)


@pytest.mark.django_db
def test_can_create_room_with_2_members():
    room = Room.objects.create(name="room name", currency="USD")
    user_1 = get_user_model().objects.create(username="testuser_1")
    user_2 = get_user_model().objects.create(username="testuser_2")
    member_1 = Member.objects.create(room=room, user=user_1)
    member_2 = Member.objects.create(room=room, user=user_2)

    assert room.member_set.count() == 2
    assert member_1.room == member_2.room


@pytest.mark.django_db
def test_can_create_spending():
    room = Room(name="room name", currency="USD")
    user = get_user_model().objects.create(username="testuser")
    member = Member(room=room, user=user)

    spending = Spending(member=member, title="some title", amount=Money(42, "USD"))

    assert spending.title == "some title"
    assert spending.member.room.name == "room name"
    assert spending.member.user.username == "testuser"


@pytest.mark.django_db
def test_can_create_dept():
    room = Room.objects.create(name="room name", currency="USD")
    user_1 = get_user_model().objects.create(username="testuser_1")
    user_2 = get_user_model().objects.create(username="testuser_2")
    member_1 = Member.objects.create(room=room, user=user_1)
    member_2 = Member.objects.create(room=room, user=user_2)

    dept = Dept(title="dept", to_member=member_1, from_member=member_2, amount=Money(10, "USD"))

    assert dept.title == "dept"
    assert dept.from_member.user.username == "testuser_2"
    assert dept.to_member.user.username == "testuser_1"
    assert dept.amount.amount == 10


@pytest.mark.django_db
def test_can_create_settlement():
    room = Room.objects.create(name="room name", currency="USD")
    user_1 = get_user_model().objects.create(username="testuser_1")
    user_2 = get_user_model().objects.create(username="testuser_2")
    member_1 = Member.objects.create(room=room, user=user_1)
    member_2 = Member.objects.create(room=room, user=user_2)

    settlement = Settlement(member=member_1, settlement_with_member=member_2, room=room)

    assert settlement.member.room.name == "room name"
    assert settlement.member.user.username == "testuser_1"
    assert settlement.settlement_with_member.user.username == "testuser_2"

    settlement.save()
    assert len(room.settlement_set.all()) == 1


@pytest.mark.django_db
def test_cant_create_dept_from_and_to_same_member():
    room = Room.objects.create(name="room name", currency="USD")
    user = get_user_model().objects.create(username="testuser")
    member = Member.objects.create(room=room, user=user)

    with pytest.raises(IntegrityError) as e_info:
        Dept.objects.create(from_member=member, to_member=member, amount=Money(10, "USD"), title="dept", room=room)
        assert "IntegrityError: CHECK constraint failed" in str(e_info.value)


@pytest.mark.django_db
def test_can_get_last_settlement():
    room = Room.objects.create(name="room name", currency="USD")
    user_1 = get_user_model().objects.create(username="testuser_1")
    user_2 = get_user_model().objects.create(username="testuser_2")
    member_1 = Member.objects.create(room=room, user=user_1)
    member_2 = Member.objects.create(room=room, user=user_2)

    Settlement.objects.create(member=member_1, settlement_with_member=member_2, room=room)
    settlement_2 = Settlement.objects.create(member=member_1, settlement_with_member=member_2, room=room)

    assert len(room.settlement_set.all()) == 2
    assert room.get_last_settlement() == settlement_2


@pytest.mark.django_db
def test_can_get_spendings_after_last_settlement():
    room = Room.objects.create(name="room name", currency="USD")
    user_1 = get_user_model().objects.create(username="testuser_1")
    user_2 = get_user_model().objects.create(username="testuser_2")
    member_1 = Member.objects.create(room=room, user=user_1)
    member_2 = Member.objects.create(room=room, user=user_2)

    Settlement.objects.create(member=member_1, settlement_with_member=member_2, room=room)
    Spending.objects.create(member=member_1, title="some title", amount=Money(42, "USD"), room=room)
    Dept.objects.create(title="dept", to_member=member_1, from_member=member_2, amount=Money(10, "USD"), room=room)

    Settlement.objects.create(member=member_1, settlement_with_member=member_2, room=room)
    spending = Spending.objects.create(member=member_1, title="some title", amount=Money(55, "USD"), room=room)
    dept = Dept.objects.create(
        title="dept", to_member=member_1, from_member=member_2, amount=Money(100, "USD"), room=room
    )

    assert len(room.settlement_set.all()) == 2
    assert len(room.spending_set.all()) == 2
    assert len(room.dept_set.all()) == 2

    last_settlement = room.get_last_settlement()
    assert list(room.get_spendings_after(last_settlement.date)) == [spending]
    assert list(room.get_depts_after(last_settlement.date)) == [dept]
