from django.contrib import admin
from spendings.models import (
    Room,
    Member,
    Spending,
    Settlement,
    Dept,
)

admin.site.register(Room)
admin.site.register(Member)
admin.site.register(Spending)
admin.site.register(Dept)
admin.site.register(Settlement)
