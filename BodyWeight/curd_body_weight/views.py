from django.shortcuts import render, redirect
from django.http import Http404
from .models import modelBodyWeight
from .forms import weightForm
from django.contrib import messages


def index(request):
    '''
    This function will get all data from dbsqlite then render into index.html
    '''
    bW = modelBodyWeight.objects.all()
    context = {
        'bodyweight': bW
    }
    return render(request, 'curd_body_weight/index.html', context)


def show(request, id):
    '''
    This function will data with selected id from dbsqlite then render into detail.html
    '''
    try:
        bw = modelBodyWeight.objects.get(pk=id)
        context = {
            'bodyweight': bw
        }
    except modelBodyWeight.DoesNotExist:
        raise Http404("Data tidak ditemukan.")
    return render(request, 'curd_body_weight/detail.html', context)

def create_view(request):
    '''
    This function show form to imput new record
    '''
    if request.method == 'POST':
        new_task = weightForm(request.POST)
        if new_task.is_valid():
            new_task.save()
            messages.success(request, 'Sukses Menambah Record baru.')
            return redirect('bodyweight:index')

    else:
        form = weightForm()
        return render(request, 'curd_body_weight/form.html', {'form': form})

def update(request, id):
    '''
    This function will allow us to update selected record
    '''
    try:
        task = modelBodyWeight.objects.get(pk=id)
    except modelBodyWeight.DoesNotExist:
        raise Http404("Record tidak ditemukan.")
    if request.method == 'POST':
        form = weightForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengubah Record.')
            return redirect('bodyweight:index')
    else:
        form = weightForm(instance=task)
    return render(request, 'curd_body_weight/form.html', {'form': form})

def delete(request, id):
    '''
    This function will delete selected record
    '''
    try:
        task = modelBodyWeight.objects.get(pk=id)
        task.delete()
        messages.success(request, 'Sukses Menghapus Record.')
        return redirect('bodyweight:index')

    except modelBodyWeight.DoesNotExist:
        raise Http404("Record tidak ditemukan.")
