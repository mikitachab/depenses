class RestApiWrapper:
    def __init__(self, client):
        self.client = client

    @property
    def user(self):
        return self.client.user

    def get_room_state(self, room_id):
        return self.make_get_request(f"room/{room_id}/state")

    def get_room_history(self, room_id):
        return self.make_get_request(f"room/{room_id}/history")

    def get_rooms_of_user(self):
        return self.make_get_request("users/rooms")

    def user_create_room(self, data):
        return self.make_post_request("users/rooms", **data)

    def make_get_request(self, endpoint):
        url = _make_api_url(endpoint)
        return self.client.get(url)

    def make_post_request(self, endpoint, **kwargs):
        url = _make_api_url(endpoint)
        return self.client.post(url, data=dict(**kwargs))

    def __getattr__(self, name):
        endpoint = _make_endpoint(name)

        if name.startswith("create_"):
            return lambda **kwargs: self.make_post_request(endpoint, **kwargs)

        if name.startswith("get_"):
            return lambda: self.make_get_request(endpoint)

        raise AttributeError(name)


def _make_endpoint(attr_name):
    endpoint = attr_name.split("_")[1]
    return endpoint if endpoint.endswith("s") else endpoint + "s"


def _make_api_url(endpoint):
    return f"/api/v1/{endpoint}/"
