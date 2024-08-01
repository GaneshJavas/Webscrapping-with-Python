from bs4 import BeautifulSoup
import requests

url = "https://www.dahuasecurity.com/in/Products/All-Products/Network-Cameras"

url_sc = requests.get(url).text
url_lxml = BeautifulSoup(url_sc,'lxml') 
# print(url_sc.content)
#print(url_lxml.prettify())

print(url_lxml.find("div", class_ = "products").prettify())