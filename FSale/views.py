from django.shortcuts import render

from .models import Produk


# Create your views here.
def index(request):
    # t = threading.Thread(target=Tokopedia, kwargs={})
    # t.setDaemon(True)
    # t.start()

    prods = Produk.objects.filter(toko__iexact= "Tokopedia")
    context = {
        'products' : prods,
    }
    return render(request, 'FSale/index.html', context)