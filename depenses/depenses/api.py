from rest_framework import routers

from spendings import api_views as spendings_views


router = routers.DefaultRouter()
router.register("rooms", spendings_views.RoomViewSet)
router.register("members", spendings_views.MemberViewSet)
router.register("spendings", spendings_views.SpendingViewSet)
router.register("depts", spendings_views.DeptViewSet)
router.register("settlements", spendings_views.SettlementViewSet)
