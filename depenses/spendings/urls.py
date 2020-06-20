from django.urls import path

import spendings.views as views

urlpatterns = [
    path("", views.hello),
]
