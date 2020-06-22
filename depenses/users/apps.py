from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_save

from users.signals import create_user_profile, save_user_profile


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
        post_save.connect(save_user_profile, sender=settings.AUTH_USER_MODEL)
