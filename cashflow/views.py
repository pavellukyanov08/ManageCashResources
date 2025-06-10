from django.shortcuts import redirect, render
from .models import *
from .forms import CashflowRecordForm


def get_cashflow_records(request):
    records = CashflowRecord.objects.all()

    return render(request, 'record_list.html', {'records': records})


def add_cashflow_record(request):
    statuses = Status.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    types = Type.objects.all()

    context = {
        'statuses': statuses,
        'categories': categories,
        'subcategories': subcategories,
        'types': types,
    }
    if request.method == 'GET':
        form = CashflowRecordForm()
        return render(request, 'record.html', {'form': form, 'context': context})

    elif request.method == 'POST':
        form = CashflowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record-list')
    else:
        form = CashflowRecordForm()

    return render(request, 'record_list.html', {'form': form})


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
