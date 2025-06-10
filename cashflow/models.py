from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')

    def __str__(self): return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self): return self.name


class CashflowRecord(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус", blank=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name="Тип", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name="Подкатегория", blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма", blank=True)
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')

    date = models.DateTimeField(verbose_name='Дата')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.type.name} - {self.amount} руб."
