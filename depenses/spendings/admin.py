from django.contrib import admin
from spendings.models import (
    Room,
    Member,
    Spending,
)

admin.site.register(Room)
admin.site.register(Member)
admin.site.register(Spending)
