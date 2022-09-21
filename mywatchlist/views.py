from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_mywatchlist(request):
    watched = 0;
    mywatchlist_data = MyWatchList.objects.all()
    for data in mywatchlist_data:
        if data.watched == "Sudah ditonton":
            watched += 1
    if watched > mywatchlist_data.count()//2:
        output = "Selamat, kamu sudah banyak menonton!"
    else:
        output = "Wah, kamu masih sedikit menonton!"
    context = {
        'list_item': mywatchlist_data,
        'nama': 'Muhammad Hafizha Dhiyaulhaq',
        'npm' : '2106750723',
        'output': output
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data  =  MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_watched(request):
    data = MyWatchList.objects.all()
    watched = 0
    for film in data:
        if film.watched == "Sudah ditonton":
            watched += 1
    if watched > data.count()//2:
        output = "Selamat, kamu sudah banyak menonton!"
    else:
        output = "Wah, kamu masih sedikit menonton!"
    context = {
        'nama' : 'Muhammad Hafizha Dhiyaulhaq',
        'npm': '2106750723',
        'output' : output,
        'watched' : watched,
        'film_count' : data.count()
    }
    return render(request, 'watchedcount.html', context)