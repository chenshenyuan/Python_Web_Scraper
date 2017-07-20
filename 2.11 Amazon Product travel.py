#not a perfect one, need improve

from bs4 import BeautifulSoup
import requests
import time

url_base = 'https://www.amazon.com/Handmade-Handbags-Fashion-Accessories/b/ref=sv_hand1_1?ie=UTF8&node='
k=1

# this while could keep in same page if didn't get the title
# helpful when some anti-scraping method detect it.
count = 0
while k<=20:
    try:
        resp = requests.get(url_base+str(k)).text
        bsobj = BeautifulSoup(resp,'lxml')
        title = bsobj.h1.b.get_text()
        print(k)
        print(title)
        k+=1
        count = 0
    except AttributeError:
        try:
            resp = requests.get(url_base + str(k)).text
            bsobj = BeautifulSoup(resp, 'lxml')
            title = bsobj.find(alt="Sorry! We couldn't find that page. Try searching or go to Amazon's home page.")
            print(k)
            print(title)
            k += 1
            count = 0
        except AttributeError:
            count +=1
            if count >=3:
                print(k)
                k+=1
                count ==0
            else:
                print('try reopen')
                print(count)
                count+=1
                time.sleep(3)

