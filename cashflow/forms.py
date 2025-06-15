from django import forms
from .models import CashflowRecord, Status, Type, Category, SubCategory

class CashflowRecordForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=True, label='Дата')

    class Meta:
        model = CashflowRecord
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        selected_type = kwargs.pop('selected_type', None)
        selected_category = kwargs.pop('selected_category', None)
        super().__init__(*args, **kwargs)

        if selected_type:
            self.fields['category'].queryset = Category.objects.filter(type_id=selected_category).order_by('name')
        else:
            self.fields['category'].queryset = Category.objects.none()

        if selected_category:
            self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=selected_category).order_by('name')
        else:
            self.fields['subcategory'].queryset = SubCategory.objects.none()
