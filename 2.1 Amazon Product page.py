from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


url_need = 'https://www.amazon.com/dp/B01K3ZR0RC'
resp = requests.get(url_need).text
bsobj = BeautifulSoup(resp,'lxml')


title = bsobj.find('div',{'id':'centerCol'}).find('span',{'id':'productTitle'}).get_text().strip()

print(title)



