from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from spendings import models


def check_member(view_func):
    def inner(*args, **kwargs):
        request = args[0]
        room_id = kwargs["room_id"]
        room = get_object_or_404(models.Room, pk=room_id)
        _check_user_is_room_member(request.user, room)
        return view_func(*args, **kwargs)
    return inner


def _check_user_is_room_member(user, room):
    room_members = room.member_set.all()
    user_members = user.member_set.all()

    if not set(room_members).intersection(set(user_members)):
        raise PermissionDenied
