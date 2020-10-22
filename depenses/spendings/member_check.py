from django.core.exceptions import PermissionDenied


def check_room_member(user, room):
    room_members = room.member_set.all()
    user_members = user.member_set.all()

    if not set(room_members).intersection(set(user_members)):
        raise PermissionDenied
