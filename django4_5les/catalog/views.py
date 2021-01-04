from django.http import HttpResponseRedirect
from django.shortcuts import render
from catalog.forms import CatalogForm
from catalog.models import Catalog


def goods_list(request):
    return render(request, 'catalog/goods_list.html', {'catalog':
                                                      Catalog.objects.all()})


def good_create(request):
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CatalogForm()

    return render(request, 'catalog/good_create.html', {'form': form})