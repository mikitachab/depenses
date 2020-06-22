import pytest
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
def test_profile_creation():
    user = User.objects.create(username="user")
    assert hasattr(user, "profile")
