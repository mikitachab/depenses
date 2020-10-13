"""depenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import spendings.room_api_views as room_views

from .api import router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("spendings.urls")),
    path("api/v1/room/<int:room_id>/state/", room_views.room_state),
    path("api/v1/room/<int:room_id>/spendings/", room_views.room_spendings),
    path("api/v1/room/<int:room_id>/depts/", room_views.room_depts),
    path("api/v1/room/<int:room_id>/settlements/", room_views.room_settlements),
    path("api/v1/", include(router.urls)),
    path("api/auth/", include("djoser.urls.authtoken")),
]
