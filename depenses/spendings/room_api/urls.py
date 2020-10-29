from django.urls import path

import spendings.room_api.views as views

urlpatterns = [
    path("<int:room_id>/state/", views.room_state),
    path("<int:room_id>/spendings/", views.room_spendings),
    path("<int:room_id>/depts/", views.room_depts),
    path("<int:room_id>/settlements/", views.room_settlements),
    path("<int:room_id>/members/", views.room_members),
    path("<int:room_id>/me/", views.room_member),
    path("<int:room_id>/history/", views.room_history),
]
