class RestApiWrapper:
    def __init__(self, client):
        self.client = client

    @property
    def user(self):
        return self.client.user

    def get_room_state(self, room_id):
        url = _make_api_url(f"room/{room_id}/state")
        return self.client.get(url).json()

    def __getattr__(self, name):
        endpoint = _make_endpoint(name)

        if name.startswith("create_"):
            return lambda **kwargs: self.client.post(_make_api_url(endpoint), data=dict(**kwargs))

        if name.startswith("get_"):
            return lambda: self.client.get(_make_api_url(endpoint))

        raise AttributeError(name)


def _make_endpoint(attr_name):
    endpoint = attr_name.split("_")[1]
    return endpoint if endpoint.endswith("s") else endpoint + "s"


def _make_api_url(endpoint):
    return f"/api/v1/{endpoint}/"
