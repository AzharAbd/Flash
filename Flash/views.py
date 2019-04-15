from django.shortcuts import render

from FSale.models import *

def index(request):
    if request.method == 'POST':
        print(request.POST['search_input'])
        prods_all = Produk.objects.filter(nama__icontains=request.POST['search_input'])
    else :
        prods_all = Produk.objects.all()
    prods_tokped = Produk.objects.filter(toko__iexact= "Tokopedia")
    time_tokped = Time.objects.get(toko__iexact="Tokopedia")
    prods_bukalapak = Produk.objects.filter(toko__iexact= "Bukalapak")
    time_bukalapak = Time.objects.get(toko__iexact="Bukalapak")
    context = {
        'products_all' : prods_all,
        'products_tokped' : prods_tokped,
        'time_tokped' : time_tokped,
        'products_bukalapak' : prods_bukalapak,
        'time_bukalapak' : time_bukalapak,
    }
    return render(request, 'index.html', context)

