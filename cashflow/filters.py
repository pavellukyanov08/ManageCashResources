import django_filters
from .models import CashflowRecord, Status, Type, Category, SubCategory
from django import forms

class CashflowRecordFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        choices=Status.objects.all(),
        label="Статус",
        empty_label="Все статусы",
    )

    type = django_filters.ChoiceFilter(
        choices=Type.objects.all(),
        label="Тип заказа",
        empty_label="Все типы",
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label="Категория",
    )

    subcategory = django_filters.ModelChoiceFilter(
        queryset=SubCategory.objects.all(),
        label="Подкатегория",
    )

    date_range = django_filters.DateFromToRangeFilter(
        field_name='date',
        label="Период",
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data.get('category'):
            # Обновляем queryset подкатегорий при наличии выбранной категории
            self.filters['subcategory'].queryset = SubCategory.objects.filter(
                category_id=self.data['category']
            )

    class Meta:
        model = CashflowRecord
        fields = []