from rest_framework.routers import DefaultRouter
from .views import CashflowRecordViewSet

router = DefaultRouter()
router.register(r'statuses', CashflowRecordViewSet, basename='status')

urlpatterns = router.urls
