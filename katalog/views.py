from gettext import Catalog
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
    'list_item': data_catalog_item,
    'nama': 'Muhammad Hafizha Dhiyaulhaq',
    'npm' : '2106750723'
    }
    return render(request, "katalog.html", context)