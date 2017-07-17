# a small program get FIX44 page link for each number and then form link to
# detail explanation.


from urllib.request import urlopen
from bs4 import BeautifulSoup


url_link = 'http://www.onixs.biz/fix-dictionary/4.4/fields_by_tag.html'
url_link_head = 'http://www.onixs.biz/fix-dictionary/4.4/'
resp = urlopen(url_link)
BsObj = BeautifulSoup(resp.read(),'lxml')

url_result = BsObj.find('p','listLinks').find_all('a') # double find_all

for obj in url_result:
    print(url_link_head + obj.attrs['href']) #obj.attrs is important to remember












