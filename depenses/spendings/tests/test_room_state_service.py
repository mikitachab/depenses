import pytest
from djmoney.money import Money

from spendings.models import Member, Room, Dept, Spending, Settlement
from spendings.services import RoomStateService


@pytest.mark.django_db
def test_can_get_spendings_after_last_settlement():
    room = Room.objects.create(name="room name", currency="USD")
    member_1 = Member.objects.create(room=room, name="user_1")
    member_2 = Member.objects.create(room=room, name="user_2")

    Settlement.objects.create(member=member_1, settlement_with_member=member_2, room=room)
    Spending.objects.create(member=member_1, title="some title", amount=Money(42, "USD"), room=room)
    Dept.objects.create(title="dept", to_member=member_1, from_member=member_2, amount=Money(10, "USD"), room=room)

    Settlement.objects.create(member=member_1, settlement_with_member=member_2, room=room)
    Spending.objects.create(member=member_1, title="some title", amount=Money(50, "USD"), room=room)
    Dept.objects.create(title="dept", to_member=member_1, from_member=member_2, amount=Money(100, "USD"), room=room)

    service = RoomStateService(room)
    state = service.calculate_room_state()
    assert state.state == {member_2: {member_1: Money(0, "USD")}, member_1: {member_2: Money(75, "USD")}}
