from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

requested_url = "http://www.pythonscraping.com/pages/page3.html"

resp = urlopen(requested_url)
bsObj = BeautifulSoup(resp,'lxml')

images = bsObj.find_all("img",{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
# two points
#/image
#/gifts
#/img+anything by .*
#.jpg
for imag in images:
    print(imag)



