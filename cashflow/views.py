from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from .models import *
from .forms import (
    CashflowRecordForm,
    TypeForm,
    StatusForm,
    CategoryForm,
    SubCategoryForm
)
from .filters import CashflowRecordFilter


def get_records(request):
    request_type = request.GET.get('entity', 'cashflow')

    records = CashflowRecord.objects.none()
    statuses = Status.objects.none()
    types = Type.objects.none()
    categories = Category.objects.none()
    subcategories = SubCategory.objects.none()

    record_filter =  None

    if request_type == 'cashflow':
        records = CashflowRecord.objects.all()
        record_filter = CashflowRecordFilter(request.GET, queryset=records)
        records = record_filter.qs

    if request_type == 'reference_books':
        statuses = Status.objects.all()
        types = Type.objects.all()
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()

    context = {
        'records': records,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        'filter': record_filter if request_type == 'cashflow' else None,
    }

    return render(request, 'record_list.html', context)


def add_record(request):
    form_type = request.GET.get('entity', 'cashflow')

    form_classes = {
        'types': TypeForm,
        'statuses': StatusForm,
        'categories': CategoryForm,
        'subcategories': SubCategoryForm,
        'cashflow': CashflowRecordForm,
    }
    form = None

    form_class = form_classes.get(form_type)

    if request.method == "POST":
        if form_class:
            form = form_class(request.POST)
            if form.is_valid():
                form.save()
                return redirect('record-list')
    else:
        form = form_class() if form_class else None

    return render(request, 'update.html', {
        'form': form,
        'form_type': form_type
    })


def filtration(request):
    queryset = CashflowRecord.objects.all()
    filter = CashflowRecordFilter(request.GET, queryset=queryset)

    return render(request, 'record_list.html', )


def edit_record(request, pk):
    entity_type = request.GET.get('entity', 'cashflow')

    _models = {
        'types': Type,
        'statuses': Status,
        'categories': Category,
        'subcategories': SubCategory,
        'cashflow': CashflowRecord,
    }

    form_classes = {
        'types': TypeForm,
        'statuses': StatusForm,
        'categories': CategoryForm,
        'subcategories': SubCategoryForm,
        'cashflow': CashflowRecordForm,
    }

    get_model = _models.get(entity_type)
    if not get_model:
        raise Http404('Неверный тип сущности')

    form_class = form_classes.get(entity_type)
    if not form_class:
        raise Http404('Форма для сущности не найдена')

    get_record = get_object_or_404(get_model, pk=pk)
    form = None

    if request.method == "POST":
        if form_class:
            form = form_class(request.POST, instance=get_record)
            if form.is_valid():
                form.save()
                return redirect('record-list')
    else:
        form = form_class(instance=get_record)

    return render(request, 'update.html', {
        'form': form,
        'form_type': entity_type
    })


def delete_record(request, pk):
    entity_type = request.GET.get('entity', 'cashflow')

    _models = {
        'types': Type,
        'statuses': Status,
        'categories': Category,
        'subcategories': SubCategory,
        'cashflow': CashflowRecord,
    }

    get_model = _models.get(entity_type)
    if not get_model:
        raise Http404('Неверный тип сущности')

    get_record = get_object_or_404(get_model, pk=pk)

    if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
        get_record.delete()
        return redirect('record-list')

    return render(request, 'delete.html', {'record': get_record})
