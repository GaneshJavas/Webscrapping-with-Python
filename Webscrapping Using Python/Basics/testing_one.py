from bs4 import BeautifulSoup
import requests

# url = "https://www.dahuasecurity.com/in/Products/All-Products/Network-Cameras"
url = "html_st.html"
with open(url,"r") as my_file:
    read_f = BeautifulSoup(my_file,'lxml')

# print(read_f.prettify())
to_match = read_f.find_all("div",class_= 'article')

for i in to_match:
    print("HeadLines: ",i.h2.text)
    print("Para: ",i.p.text)