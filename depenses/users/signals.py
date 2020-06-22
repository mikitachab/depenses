from django.apps import apps


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile = apps.get_model("users.Profile")
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
