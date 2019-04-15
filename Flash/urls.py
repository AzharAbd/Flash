
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^FSale/', include('FSale.urls'))
]

from FSale.models import Produk
from FSale.flashscrape import *
import threading

t1 = threading.Thread(target=Tokopedia, kwargs={})
t1.setDaemon(True)
t1.start()

t2 = threading.Thread(target=Bukalapak, kwargs={})
t2.setDaemon(True)
t2.start()