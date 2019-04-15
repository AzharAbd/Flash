import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from getpass import getpass


from .models import *


def Bukalapak():
    while (True):
        print(Bukalapak)
        #open chromedriver
        driver = webdriver.Chrome('/home/azhar/Dev/Flash/FSale/chromedriver')
        #go to the link
        driver.get('https://www.bukalapak.com/flash-deal')
        #get client side html
        source_code = driver.execute_script('return document.documentElement.outerHTML;')
        driver.quit()
        #parse html to text
        soup = BeautifulSoup(source_code, 'html.parser')

        #scrape time
        try:
            time_container = soup.find('span', {'class' : 'u-txt--medium u-fg--red-brand u-txt--bold'}).string
            time_container = time_container.replace(" ", "")
            time = time_container.split(":")
            hour = time[0]
            minute = time[1]
            second = time[2]
            Time.objects.filter(toko = "Bukalapak").delete()
            Time.objects.create(hour = hour, minute = minute, second = second, toko = "Bukalapak")   
        except:
            pass

        #scrape product info
        elementExist = True
        try :
            products = soup.find_all('div',{'class' : 'c-card c-card--flash-deal'})
        except :
            elementExist = False
        if (elementExist):
            Produk.objects.filter(toko = "Bukalapak").delete()
            for product in products:
                img_container = product.find('div',{'class' : 'c-card__head'})
                img = img_container.find('img')['src']
                
                info_container = product.find('div',{'class' : 'c-card__body'})
                desc = info_container.find('div', {'class': 'c-card--flash-deal__ellipsis-2 u-txt--small u-fg--black u-mrgn-bottom--1'}).string
                before_price = info_container.find('span', {'class' : 'c-product-price__original u-mrgn-right--0'}).string
                after_price = info_container.find('span', {'class': 'c-product-price__reduced u-fg--red-brand'}).string
                stock = info_container.find('div', {'class' : 'u-txt--tiny u-fg--black'}).string
            
                Produk.objects.create(nama = desc, img = img, before_price = before_price, after_price =  after_price, url ='', stock= stock,toko = "Bukalapak")
        sleep(300)


def Tokopedia():
    while (True):
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
            hour = int(time_set[0].string)*10 + int(time_set[2].string)
            minute = int(time_set[4].string)*10 + int(time_set[6].string)
            second = int(time_set[8].string)*10 + int(time_set[10].string)
        except:
            hour = 0
            minute = 0
            second = 0
        Time.objects.filter(toko = "Tokopedia").delete()
        Time.objects.create(hour = hour, minute = minute, second = second, toko ="Tokopedia")

        elementExist = True
        try :
            container = soup.find('div',{'class' : 'td_row td_container_free'})
        except:
            elementExist = False

        if (elementExist):
            i = 0
            try :
                products = container.find_all('div',{'class' : 'product-card product-card-identity'})
            except:
                elementExist =  False
            if (elementExist):
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
                    Produk.objects.create(nama = desc,img = imgs, after_price = after_prices, before_price = before_prices, stock = stocks, url = redirect_link, toko = "Tokopedia" )
        sleep(300)