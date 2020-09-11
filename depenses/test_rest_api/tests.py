def test_can_create_room(logged_in_api_client):
    room_name = "testroom"
    room_currency = "PLN"

    post_resp = logged_in_api_client.create_room(name=room_name, currency=room_currency)
    assert post_resp.status_code == 201

    get_resp = logged_in_api_client.get_rooms()
    assert len(get_resp.json()) == 1

    room = get_resp.json()[0]
    assert room["name"] == room_name
    assert room["currency"] == room_currency


def test_can_create_member(logged_in_api_client):
    room_name = "testroom"
    room_currency = "PLN"

    logged_in_api_client.create_room(name=room_name, currency=room_currency)

    member_post_resp = logged_in_api_client.create_member(name="test", room=1)
    assert member_post_resp.status_code == 201


def test_can_create_spending(logged_in_api_client):
    room_name = "testroom"
    room_currency = "PLN"

    logged_in_api_client.create_room(name=room_name, currency=room_currency)

    member_post_resp = logged_in_api_client.create_member(name="test", room=1)

    member_id = member_post_resp.json()["id"]
    resp = logged_in_api_client.create_spending(title="test", amount=1, member=member_id)
    assert resp.status_code == 201


def test_can_create_dept(logged_in_api_client):
    room_name = "testroom"
    room_currency = "PLN"

    logged_in_api_client.create_room(name=room_name, currency=room_currency)

    member_post_resp_1 = logged_in_api_client.create_member(name="test", room=1)
    member_post_resp_2 = logged_in_api_client.create_member(name="test_1", room=1)

    member_1_id = member_post_resp_1.json()["id"]
    member_2_id = member_post_resp_2.json()["id"]
    resp = logged_in_api_client.create_dept(title="test", amount=1, from_member=member_1_id, to_member=member_2_id)

    assert resp.status_code == 201
