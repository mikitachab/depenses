from collections import defaultdict

from djmoney.money import Money

from .utils import make_pipeline


class RoomStateService:
    def __init__(self, room):
        self.room = room
        self.members = list(self.room.member_set.all())
        self._room_zero = Money(0, self.room.currency)
        last_settlement = self.room.get_last_settlement()
        self._last_settlement_date = last_settlement.date if last_settlement else None

    def add_spendgins(self, current_result):
        result = dict(current_result)
        spendings = self.room.get_spendings_after(self._last_settlement_date)
        for s in spendings:
            amount = s.amount / len(self.members)
            for m in [m for m in self.members if m != s.member]:
                result[m][s.member] += amount
        return result

    def add_depts(self, current_result):
        result = dict(current_result)
        depts = self.room.get_depts_after(self._last_settlement_date)
        for dept in depts:
            result[dept.to_member][dept.from_member] += dept.amount
        return result

    def reduce_depts(self, current_result):
        result = dict(current_result)
        for m in self.members:
            for k, amount in result[m].items():
                if amount > result[k][m]:
                    result[m][k] -= result[k][m]
                    result[k][m] = self._room_zero
                else:
                    result[k][m] -= result[m][k]
                    result[m][k] = self._room_zero
        return result

    def calculate_room_state(self):
        result = {member: defaultdict(int) for member in self.members}
        pipeline = make_pipeline([self.add_spendgins, self.add_depts, self.reduce_depts])
        return RoomState(pipeline(result))


class RoomState:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

    def to_json(self):
        return {
            member.user.username: {
                other_member.user.username: dept.amount for other_member, dept in members_depts.items()
            }
            for member, members_depts in self._state.items()
        }
