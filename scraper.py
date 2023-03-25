from bs4 import BeautifulSoup
import requests

url = "https://www.cardekho.com/maruti/swift"
headers = {'User-Agent':'Google Chrome Version 111.0.5563.65 (Official Build) (64-bit)'}

response=requests.get(url,headers=headers)


soup=BeautifulSoup(response.content,'lxml')

car_title=soup.select('gsc_col-xs-12 gsc_col-sm-12 gsc_col-md-7 gsc_col-lg-7 overviewdetail')[0].get_text().strip()
print(car_title)