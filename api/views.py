from rest_framework import viewsets
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

class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        type_id = self.request.query_params.get('type')
        if type_id:
            return Category.objects.filter(type_id=type_id)
        return Category.objects.all()

class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        if category_id:
            return SubCategory.objects.filter(category_id=category_id)
        return SubCategory.objects.all()


class CashflowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CashflowRecord.objects.all().order_by('-date')
    serializer_class = CashflowSerializer
    # filters_backends = [DjangoFilterBackend]
    # filterset_fields = ['status', 'type', 'sub_category', 'category', 'custom_date']
