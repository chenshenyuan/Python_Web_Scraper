# use urllib and beautiful soup to get the header of the page
# use a function to get rid of some possible error

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

def get_header(input_url):
     try:
          r = urlopen(input_url)
     except HTTPError: #if the address is error
          return None
     try:
          bsObj = BeautifulSoup(r.read(), 'lxml')
          header = bsObj.h1.text
     except AttributeError: # if the object does not have the attribution
          return None
     return header

page_header = get_header('https://en.wikipedia.org/wiki/George_Washington')
print(page_header)
page_header = get_header('https://en.wikipedia.org/wiki/Geor')
print(page_header)
