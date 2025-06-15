from rest_framework import serializers
from cashflow.models import *



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashflowRecord
        fields = '__all__'

    def validate(self, data):
        if data['category'].type != data['type']:
            raise serializers.ValidationError('Категория не относится к указанному типу')
        if data['subcategory'].category != data['category']:
            raise serializers.ValidationError("Подкатегория не относится к указанной категории.")
        return data