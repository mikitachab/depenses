from spendings import models, serializers


class RoomHistoryService:
    def __init__(self, room):
        self.room = room

    def get_history(self):
        depts = list(self.room.dept_set.all())
        spendings = list(self.room.spending_set.all())
        settlements = list(self.room.settlement_set.all())

        history = sorted(depts + spendings + settlements, key=lambda x: x.date, reverse=True)

        return RoomHistory(history)


class RoomHistory:
    def __init__(self, history):
        self._history = history

    def history(self):
        return self._history

    def to_json(self):
        return [_serialize_history_item(item) for item in self._history]


def _serialize_history_item(item):
    data = {}
    if isinstance(item, models.Dept):
        data = serializers.DeptSerializer(item).data
        data["type"] = "dept"
    if isinstance(item, models.Spending):
        data = serializers.SpengingSerializer(item).data
        data["type"] = "spending"
    if isinstance(item, models.Settlement):
        data = serializers.SettlementSerializer(item).data
        data["type"] = "settlement"
    return data
