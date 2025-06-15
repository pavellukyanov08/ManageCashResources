from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import (
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

urlpatterns = [
    path('records/', views.get_cashflow_records, name='record-list'),
    path('records/create/', views.add_cashflow_record, name='record-create'),
    path('records/<int:pk>/update', views.edit_cashflow_record, name='record-update'),
    path('records/<int:pk>/delete', views.delete_cashflow_record, name='record-delete'),

    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
]
