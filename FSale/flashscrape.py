import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from getpass import getpass
from datetime import datetime


from .models import *

def Blibli(idx):
    global hour
    global minute
    global second
    global periodIdx
    print(Blibli)
    now = datetime.now()
    t = ((now.hour+7)%24) * 3600 + now.minute*60 + now.second
    print(t)
    print(now.hour)
    print(now.minute)
    print(now.second)
    period = [21600,43200,64800]
    endperiod = [43200, 64800,86400,21600]
    harusDelete = False
    kebalik = False
    if (t >= period[2]):
        if (periodIdx != 2):
            harusDelete = True
        periodIdx = 2
    elif (t >= period[1]):
        if (periodIdx != 1):
            harusDelete = True
        periodIdx=1
    elif (t >= period[0]):
        if (periodIdx != 0):
            harusDelete =  True
        periodIdx = 0
    else:
        if (periodIdx != 2):
            harusDelete = True
        periodIdx = 2
        kebalik = True
    
    if (kebalik):
        deltaT = endperiod[periodIdx+1] - t
    else :
        deltaT= endperiod[periodIdx] - t
    hour[idx] = int(deltaT / 3600)
    minute[idx] = int ((deltaT % 3600)/60)
    second[idx] = int (deltaT % 60)
    print(hour[idx])
    print(minute[idx])
    print(second[idx])
    time = Time.objects.get(toko ="Blibli")
    time.hour = hour[idx]
    time.minute = minute[idx]
    time.second = second[idx]
    time.save()
    #open chromedriver
    driver = webdriver.Chrome('/home/azhar/Dev/Flash/FSale/chromedriver')
    #go to the link
    driver.get('https://www.blibli.com/promosi/flashsale?appsWebview=true')
    #get client side html
    source_code = driver.execute_script('return document.documentElement.outerHTML;')
    driver.quit()
    #parse html to text
    soup = BeautifulSoup(source_code, 'html.parser')

    # if (harusDelete):
    Produk.objects.filter(toko = "Blibli").delete()

    #scrape products
    products_containers = soup.find_all('div',{'class' : 'product-set-list'})
    for products_container in products_containers:
        products = products_container.find_all('a' ,{'class' : 'single-product'})
        for product in products:
            try:
                try :
                    url = product['href']
                except:
                    url = ''
                    print("href tidak ada")
                img = product.find('img')['data-original']
                desc = product.find('div',{'class':'product-title'}).string
                try:
                    before_price = product.find('span',{'class':'old-price-text'}).string
                except :
                    before_price = "None"
                    print("before_price not found")
                after_price = product.find('span',{'class':'new-price-text'}).string
                stock ="Tersedia"
                # if (harusDelete):
                try:
                    Produk.objects.create(nama = desc, img = img, before_price = before_price, after_price =  after_price, url =url, stock= stock,toko = "Blibli")
                except :
                    print("ada karakter yang tidak diketahui di info produk")
                    pass
                # else :
                #     produk = Produk.objects.get(nama = desc)
                #     produk.stock = stock
                #     produk.save()

            except:
                print("tidak ada produk")
                pass
        
def Bukalapak(idx):
    global hour
    global minute
    global second
    print(Bukalapak)
    #open chromedriver
    driver = webdriver.Chrome('/home/azhar/Dev/Flash/FSale/chromedriver')
    #go to the link
    driver.get('https://www.bukalapak.com/flash-deal')
    #get client side html
    source_code = driver.execute_script('return document.documentElement.outerHTML;')
    sleep(3)
    driver.quit()
    #parse html to text
    soup = BeautifulSoup(source_code, 'html.parser')
    

    #scrape time
    try:
        time_container = soup.find('span', {'class' : 'u-txt--medium u-fg--red-brand u-txt--bold'}).string
        time_container = time_container.replace(" ", "")
        print(time_container)
        time = time_container.split(":")
        tBefore = int(hour[idx]) * 3600 + int(minute[idx]) * 60 + int(second[idx])
        hour[idx] = time[0]
        minute[idx] = time[1]
        second[idx] = time[2]
        tAfter = int(hour[idx]) * 3600 + int(minute[idx]) * 60 + int(second[idx])
        harusDelete = tAfter > tBefore
        time = Time.objects.get(toko = "Bukalapak")
        time.hour = hour[idx]
        time.minute = minute[idx]
        time.second =  second[idx]
        time.save()
        # Time.objects.filter(toko = "Bukalapak").delete()
        # Time.objects.create(hour = hour, minute = minute, second = second, toko = "Bukalapak")   
    except:
        harusDelete = True
        print("failed to scrape time Bukalapak")

    try:
        stats_container = soup.find('li', {'class' : 'c-tab__list c-tab__list--inside o-layout__item u-width-2of10 u-mrgn--0 is-active'})
        stats = stats_container.find('div',{'class' : 'u-txt--bold'}).string
    except:
        print("flash sale baru ada besok")
        stats = "Besok"

    if (stats != "Sekarang"):
        Produk.objects.filter(toko ="Bukalapak").delete()
        status = "Starts in"
    else :
        #scrape product info
        elementExist = True
        try :
            products = soup.find_all('div',{'class' : 'c-card c-card--flash-deal'})
        except :
            elementExist = False
            print("tidak ada barang")
        if (elementExist):
            if (harusDelete):
                Produk.objects.filter(toko = "Bukalapak").delete()
            for product in products:
                img_container = product.find('div',{'class' : 'c-card__head'})
                img = img_container.find('img')['src']
                
                info_container = product.find('div',{'class' : 'c-card__body'})
                desc = info_container.find('div', {'class': 'c-card--flash-deal__ellipsis-2 u-txt--small u-fg--black u-mrgn-bottom--1'}).string
                before_price = info_container.find('span', {'class' : 'c-product-price__original u-mrgn-right--0'}).string
                after_price = info_container.find('span', {'class': 'c-product-price__reduced u-fg--red-brand'}).string
                stock = info_container.find('div', {'class' : 'u-txt--tiny u-fg--black'}).string
                if (harusDelete):
                    Produk.objects.create(nama = desc, img = img, before_price = before_price, after_price =  after_price, url ='', stock= stock,toko = "Bukalapak")
                else :
                    produk = Produk.objects.get(nama = desc)
                    produk.stock = stock
                    produk.save()


def Tokopedia(idx):
    global hour
    global minute
    global second
    print(Tokopedia)
    #open chromedriver
    driver = webdriver.Chrome('/home/azhar/Dev/Flash/FSale/chromedriver')
    #go to the link
    driver.get('https://www.tokopedia.com/discovery/flash-sale')
    #scroll down to the bottom of the page
    for i in range (50):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.075)
    #get client side html
    source_code = driver.execute_script('return document.documentElement.outerHTML;')
    driver.quit()
    #parse html to text
    soup = BeautifulSoup(source_code, 'html.parser')
    try:
        counter = soup.find('span',{'id' : 'sprintsale-counter'})
        time_set = counter.find_all('li')
        tBefore = hour[idx] * 3600 + minute[idx] * 60 + second[idx]
        hour[idx] = int(time_set[0].string)*10 + int(time_set[2].string)
        minute[idx] = int(time_set[4].string)*10 + int(time_set[6].string)
        second[idx] = int(time_set[8].string)*10 + int(time_set[10].string)
        tAfter = hour[idx] * 3600 + minute[idx] * 60 + second[idx]
        harusDelete =  tAfter > tBefore
        time = Time.objects.get(toko = "Tokopedia")
        time.hour = hour[idx]
        time.minute = minute[idx]
        time.second = second[idx]
        time.save()
        print(time.second)
    except:
        harusDelete = True
        print("scrape time gagal")
    # Time.objects.filter(toko = "Tokopedia").delete()
    # Time.objects.create(hour = hour, minute = minute, second = second, toko ="Tokopedia")

    elementExist = True
    try :
        container = soup.find('div',{'class' : 'td_row td_container_free'})
    except:
        elementExist = False
        print("tidak ada produks")
    if (elementExist):
        i = 0
        try :
            products = container.find_all('div',{'class' : 'product-card product-card-identity'})
        except:
            elementExist =  False
            print("tidak ada produk")
        if (elementExist):
            if (harusDelete) :
                Produk.objects.filter(toko = "Tokopedia").delete()
            for product in products:
                # print(product)
                redirect_link = product.find('a')['href']
                desc = product.find('h1').string           
                imgs = product.find('img')['src']
                after_prices = product.find('div',{'class' : 'price-after'}).string
                before_prices = product.find('div',{'class' : 'price-before'}).string
                stock_all_info = product.find('div',{'class' : 'stock-info'})
                try:
                    stocks = stock_all_info.find('div',{'class' : 'stock-info'}).string
                except:
                    stocks="Hampir habis"
                if (harusDelete):
                    Produk.objects.create(nama = desc,img = imgs, after_price = after_prices, before_price = before_prices, stock = stocks, url = redirect_link, toko = "Tokopedia" )
                else :
                    produk = Produk.objects.get(nama = desc)
                    produk.stock = stocks
                    produk.save()

def scrape():
    while True:
        Tokopedia(0)
        Bukalapak(1)
        Blibli(2)
        sleep(300)

hour = [0,0,0]
minute = [0,0,0]
second = [0,0,0]

periodIdx = 3