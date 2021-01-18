from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from catalog.forms import CatalogForm
from catalog.models import Catalog


def goods_list(request):
    return render(request, 'catalog/goods_list.html', {'catalog':
                                                      Catalog.objects.all()})


def good_create(request):
    data = dict()
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Catalog.objects.all()
            data['products_html'] = render_to_string('catalog/list.html',
                                                     {'catalog': products})
        else:
            data['form_html'] = render_to_string('catalog/good_create.html',
                                                 {'form': form},
                                                 request=request)

    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('catalog/good_create.html',
                                             {'form': CatalogForm()},
                                             request=request)

    return JsonResponse(data)