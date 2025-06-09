from rest_framework import serializers
from .models import *


class CashflowRecordsSerializer(serializers.ModelSerializer):
    # model = CashflowRecord
    # fields = '__all__'

    class Meta:
        model = CashflowRecord