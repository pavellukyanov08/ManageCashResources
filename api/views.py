from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    CashflowSerializer,
    CategorySerializer,
    TypeSerializer,
    SubCategorySerializer,
    StatusSerializer
)
from cashflow.models import (
    Status,
    Type,
    Category,
    SubCategory,
    CashflowRecord
)

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        type_id = self.request.query_params.get('type')
        if type_id:
            return Category.objects.filter(type_id=type_id)
        return Category.objects.all()

class SubCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        if category_id:
            return SubCategory.objects.filter(category_id=category_id)
        return SubCategory.objects.all()


class CashflowViewSet(viewsets.ModelViewSet):
    queryset = CashflowRecord.objects.all().order_by('-date')
    serializer_class = CashflowSerializer
    permission_classes = [IsAuthenticated]
    # filters_backends = [DjangoFilterBackend]
    # filterset_fields = ['status', 'type', 'sub_category', 'category', 'custom_date']
