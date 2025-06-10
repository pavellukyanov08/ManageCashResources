from django import forms
from .models import CashflowRecord, Status, Type, Category, SubCategory

class CashflowRecordForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=True, label='Дата')

    class Meta:
        model = CashflowRecord
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = SubCategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type).order_by('name')

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['subcategory'].queryset = SubCategory.objects.filter(category=self.instance.category).order_by('name')
