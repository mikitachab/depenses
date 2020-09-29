import pytest

from .rest_api_wrapper import RestApiWrapper


@pytest.fixture
def logged_in_client(client, django_user_model):
    username = "testname"
    password = "test1234567"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    client.user = user
    return client


@pytest.fixture
def logged_in_api_client(logged_in_client):
    return RestApiWrapper(logged_in_client)
