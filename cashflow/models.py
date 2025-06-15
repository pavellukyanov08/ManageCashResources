from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self): return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self): return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')

    created_at = models.DateField(auto_now_add=True)

    def __str__(self): return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    created_at = models.DateField(auto_now_add=True)

    def __str__(self): return self.name


class CashflowRecord(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name="Тип", blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name="Подкатегория")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')

    date = models.DateTimeField(verbose_name='Дата')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        type_name = self.type.name if self.type_id and self.type else 'Без типа'
        return f"{self.date} - {type_name} - {self.amount}"
