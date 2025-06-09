from rest_framework import viewsets
from .models import *
from .serializers import CashflowRecordsSerializer

class CashflowRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = CashflowRecordsSerializer
