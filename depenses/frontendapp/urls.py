from django.urls import path

import frontendapp.views as views

urlpatterns = [
    path("", views.serve_react_app),
]
