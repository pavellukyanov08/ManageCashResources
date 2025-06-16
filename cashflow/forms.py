from django import forms
from .models import CashflowRecord, Type, Category, SubCategory, Status


class CashflowRecordForm(forms.ModelForm):
    class Meta:
        model = CashflowRecord
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = SubCategory.objects.none()

        if self.data:
            if 'type' in self.data:
                try:
                    type_id = int(self.data.get('type'))
                    self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
                except (ValueError, TypeError):
                    pass

            if 'category' in self.data:
                try:
                    category_id = int(self.data.get('category'))
                    self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
                except (ValueError, TypeError):
                    pass

        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)
            self.fields['subcategory'].queryset = SubCategory.objects.filter(category=self.instance.category)


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].queryset = Type.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        type_obj = cleaned_data.get('type')

        if name and type_obj:
            if Category.objects.filter(
                    name=name,
                    type=type_obj
            ).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(
                    "Тип с таким именем уже существует в этой категории"
                )

        return cleaned_data


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')

        if name and category:
            if SubCategory.objects.filter(
                    name=name,
                    category=category
            ).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(
                    "Подкатегория с таким именем уже существует в этой категории"
                )

        return cleaned_data
