from bs4 import BeautifulSoup
import requests

def sub_folder(m_folder):
    for i in m_folder: print(i)



url = "https://www.dahuasecurity.com/in/products/All-Products/Network-Cameras/WizMind-Series/Panoramic-Series/Hubble-Series/PSDW83242M-A360-D845L-S3=S3"

url_sc = requests.get(url).text
url_lxml = BeautifulSoup(url_sc,'lxml') 
# print(url_sc.content)
#print(url_lxml.prettify())

#print(url_lxml.find("div", class_ = "products").prettify())
main_links = []

for i in url_lxml.find_all("li", class_ = "product-self"):
    main_links.append({"name" : i.text.strip('Learn More'), "link" : f"https://www.dahuasecurity.com{i.a['href']}", "i_link" : i.img['src']})

sub_folder(main_links)
