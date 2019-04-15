from django.db import models

# Create your models here.
class Produk(models.Model):
    nama = models.CharField(max_length=512)
    img = models.CharField(max_length=1024, default = 'img/product/p1.jpg')
    after_price = models.CharField(max_length = 50, default = '150.000')
    before_price = models.CharField(max_length = 50, default = '210.000')
    stock = models.CharField(max_length=50, default = 'Terjual sebagian')
    url = models.CharField(max_length =1024, default = '')
    toko = models.CharField(max_length=255, default = 'Tokopedia')

    def __str__(self):
        return "{}.{}".format(self.id,self.nama)

class Time(models.Model):
    hour = models.CharField(max_length=2, default ='0')
    minute = models.CharField(max_length=2, default ='0')
    second = models.CharField(max_length=2, default ='0')
    toko = models.CharField(max_length=255, default = 'Tokopedia')

    def __str__(self):
        return "{}.{}".format(self.id, self.toko)