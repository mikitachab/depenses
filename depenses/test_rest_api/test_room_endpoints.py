def test_can_get_room_state(logged_in_api_client, django_user_model, room):
    logged_in_api_client.create_room(name=room.name, currency=room.currency)

    user_1 = logged_in_api_client.user
    user_2 = django_user_model.objects.create(username="test_1")
    member_post_resp_1 = logged_in_api_client.create_member(user=user_1.id, room=1, name="test_1")
    member_post_resp_2 = logged_in_api_client.create_member(user=user_2.id, room=1, name="test_2")

    member_1_id = member_post_resp_1.json()["id"]
    member_2_id = member_post_resp_2.json()["id"]
    logged_in_api_client.create_dept(title="test", amount=20, from_member=member_1_id, to_member=member_2_id, room=1)
    logged_in_api_client.create_spending(title="test", amount=10, member=member_2_id, room=1)

    room_state = logged_in_api_client.get_room_state(room_id=1)
    assert room_state == {"test_1": {"test_2": 0.0}, "test_2": {"test_1": 15.0}}


def test_can_get_room_state_one_spending(logged_in_api_client, django_user_model, room):
    logged_in_api_client.create_room(name=room.name, currency=room.currency)

    user_1 = logged_in_api_client.user
    user_2 = django_user_model.objects.create(username="test_1")
    logged_in_api_client.create_member(user=user_1.id, room=1, name="test_1")
    member_post_resp_2 = logged_in_api_client.create_member(user=user_2.id, room=1, name="test_2")

    member_2_id = member_post_resp_2.json()["id"]
    logged_in_api_client.create_spending(title="test", amount=10, member=member_2_id, room=1)

    room_state = logged_in_api_client.get_room_state(room_id=1)
    assert room_state == {"test_1": {"test_2": 5.0}, "test_2": {"test_1": 0.0}}
