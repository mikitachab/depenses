import functools

from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.decorators import api_view, permission_classes

from spendings import models


def room_endpoint(methods, permission_classes_):
    def room_endpoint_decorator(view_func):
        @api_view(methods)
        @permission_classes(permission_classes_)
        @functools.wraps(view_func)
        def inner(*args, **kwargs):
            request = args[0]
            room_id = kwargs["room_id"]
            room = get_object_or_404(models.Room, pk=room_id)
            _check_user_is_room_member(request.user, room)
            del kwargs["room_id"]
            return view_func(*args, room=room, **kwargs)

        return inner

    return room_endpoint_decorator


def _check_user_is_room_member(user, room):
    room_members = room.member_set.all()
    user_members = user.member_set.all()

    if not set(room_members).intersection(set(user_members)):
        raise PermissionDenied
