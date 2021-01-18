from django.urls import path
from catalog.views import goods_list, good_create

app_name = 'catalog'

urlpatterns = [
    path('', goods_list, name='goods_list'),
    path('good_create', good_create, name='good_create'),
]

