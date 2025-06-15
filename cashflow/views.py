from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import CashflowRecordForm


def get_cashflow_records(request):
    records = CashflowRecord.objects.all()
    type =

    return render(request, 'record_list.html', {'records': records})


def load_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)


def add_cashflow_record(request):
    selected_type = request.POST.get('type')
    selected_category = request.POST.get('category')

    form_kwargs = {}
    if selected_type:
        form_kwargs['selected_type'] = selected_type
    if selected_category:
        form_kwargs['selected_category'] = selected_category

    if request.method == 'POST':
        form = CashflowRecordForm(request.POST, **form_kwargs)
        if form.is_valid():
            form.save()
            return redirect('record-list')
    else:
        form = CashflowRecordForm()

    return render(request, 'record.html', {'form': form})


def edit_cashflow_record(request, record_id):
    record = CashflowRecord.objects.get(record_id=record_id)
    if request.method == 'PUT':
        form = CashflowRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record-list')
    else:
        form = CashflowRecordForm(instance=record)

    return render(request, 'update.html', {'form': form})


def delete_cashflow_record(request, record_id):
    record = CashflowRecord.objects.get(record_id=record_id)
    if request.method == 'DELETE':
        form = CashflowRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record-list')
    else:
        form = CashflowRecordForm(instance=record)

    return render(request, 'update.html', {'form': form})
