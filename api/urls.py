from rest_framework.routers import DefaultRouter

from .views import (
    StatusViewSet,
    TypeViewSet,
    CategoryViewSet,
    SubCategoryViewSet,
    CashflowViewSet
)

router = DefaultRouter()
router.register(r'statuses', StatusViewSet, basename='status')
router.register(r'types', TypeViewSet, basename='type')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')
router.register(r'cashflows', CashflowViewSet, basename='cashflow')

urlpatterns = router.urls