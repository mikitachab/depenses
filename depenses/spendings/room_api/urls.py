from django.urls import path

import spendings.room_api.views as views
from spendings.room_api.history_api_view import room_history

urlpatterns = [
    path("<int:room_id>/state/", views.room_state),
    path("<int:room_id>/spendings/", views.room_spendings),
    path("<int:room_id>/depts/", views.room_depts),
    path("<int:room_id>/settlements/", views.room_settlements),
    path("<int:room_id>/members/", views.room_members),
    path("<int:room_id>/history/", room_history),
]
