from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import (
    CashflowSerializer,
    CategorySerializer,
    TypeSerializer,
    SubCategorySerializer,
    StatusSerializer
)


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CashflowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CashflowRecord.objects.all().order_by('-date')
    serializer_class = CashflowSerializer
    filters_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'type', 'sub_category', 'category', 'custom_date']
