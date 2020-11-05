import pytest

from spendings import models, serializers


@pytest.mark.django_db
def test_can_get_rooms_of_user(logged_in_api_client):
    user = logged_in_api_client.user
    room_1 = models.Room.objects.create(name="test_1", currency="PLN")
    models.Member.objects.create(room=room_1, user=user, name="test_1")
    room_2 = models.Room.objects.create(name="test_1", currency="PLN")
    models.Member.objects.create(room=room_2, user=user, name="test_2")

    user_rooms = logged_in_api_client.get_rooms_of_user()

    assert user_rooms.json() == [
        serializers.RoomSerializer(room_1).data,
        serializers.RoomSerializer(room_2).data
    ]


@pytest.mark.django_db
def test_can_create_room(logged_in_api_client):
    created_room = logged_in_api_client.user_create_room(data=dict(name="testname", currency="USD"))
    user_rooms = logged_in_api_client.get_rooms_of_user()
    assert user_rooms.json() == [created_room.json()]
