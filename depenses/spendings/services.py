from dataclasses import dataclass
from collections import defaultdict

from djmoney.money import Money


class RoomStateService:
    def __init__(self, room):
        self.room = room
        self.members = list(self.room.member_set.all())
        self._zero = Money(0, self.room.currency)

    def calculate_room_state(self):
        last_settlement = self.room.get_last_settlement()
        depts = self.room.get_depts_after(last_settlement.date)
        spendings = self.room.get_spendings_after(last_settlement.date)

        members = list(self.room.member_set.all())

        result = {member: defaultdict(int) for member in members}

        for s in spendings:
            amount = s.amount / len(members)
            for m in [m for m in members if m != s.member]:
                result[m][s.member] += amount

        for d in depts:
            result[d.to_member][d.from_member] += d.amount

        for m in members:
            for k, amount in result[m].items():
                if amount > result[k][m]:
                    result[m][k] -= result[k][m]
                    result[k][m] = self._zero
                else:
                    result[k][m] -= result[m][k]
                    result[m][k] = self._zero

        return result
