def test_can_create_room(logged_in_api_client, room):
    post_resp = logged_in_api_client.create_room(name=room.name, currency=room.currency)
    assert post_resp.status_code == 201

    get_resp = logged_in_api_client.get_rooms()
    assert len(get_resp.json()) == 1

    new_room = get_resp.json()[0]
    assert new_room["name"] == room.name
    assert new_room["currency"] == room.currency


def test_can_create_member(logged_in_api_client, room):
    logged_in_api_client.create_room(name=room.name, currency=room.currency)
    user = logged_in_api_client.user
    member_post_resp = logged_in_api_client.create_member(user=user.id, room=1, name="test")
    resp_json = member_post_resp.json()
    assert member_post_resp.status_code == 201
    assert resp_json["id"] == 1
    assert resp_json["name"] == "test"


def test_can_create_spending(logged_in_api_client, room):
    logged_in_api_client.create_room(name=room.name, currency=room.currency)

    user = logged_in_api_client.user
    member_post_resp = logged_in_api_client.create_member(user=user.id, room=1, name="test")

    member_id = member_post_resp.json()["id"]
    resp = logged_in_api_client.create_spending(title="test", amount=1, member=member_id, room=1)
    assert resp.status_code == 201


def test_can_create_dept(logged_in_api_client, django_user_model, room):
    logged_in_api_client.create_room(name=room.name, currency=room.currency)

    user_1 = logged_in_api_client.user
    user_2 = django_user_model.objects.create(username="test_1")
    member_post_resp_1 = logged_in_api_client.create_member(user=user_1.id, room=1, name="test")
    member_post_resp_2 = logged_in_api_client.create_member(user=user_2.id, room=1, name="test")

    member_1_id = member_post_resp_1.json()["id"]
    member_2_id = member_post_resp_2.json()["id"]
    resp = logged_in_api_client.create_dept(
        title="test", amount=1, from_member=member_1_id, to_member=member_2_id, room=1
    )

    assert resp.status_code == 201


def test_can_get_room_state(logged_in_api_client, django_user_model, room):
    logged_in_api_client.create_room(name=room.name, currency=room.currency)

    user_1 = logged_in_api_client.user
    user_2 = django_user_model.objects.create(username="test_1")
    member_post_resp_1 = logged_in_api_client.create_member(user=user_1.id, room=1, name="test")
    member_post_resp_2 = logged_in_api_client.create_member(user=user_2.id, room=1, name="test")

    member_1_id = member_post_resp_1.json()["id"]
    member_2_id = member_post_resp_2.json()["id"]
    logged_in_api_client.create_dept(title="test", amount=20, from_member=member_1_id, to_member=member_2_id, room=1)
    logged_in_api_client.create_spending(title="test", amount=10, member=member_2_id, room=1)

    room_state = logged_in_api_client.get_room_state(room_id=1)
    assert room_state == {user_1.username: {user_2.username: 0.0}, user_2.username: {user_1.username: 15.0}}
