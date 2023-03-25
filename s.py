from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urReq
car = "https://www.cardekho.com/"
car

response_website = urReq(car)
response_website.read()
