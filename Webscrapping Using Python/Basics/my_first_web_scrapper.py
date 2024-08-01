import urllib.request 

for i in range(1,10):
    try:
        read_html = urllib.request.urlopen(f"https://pythonscraping.com/pages/page{i}.html")
        print(f"LOADING PAGE {i}")
        print(read_html.read())
    except urllib.error.HTTPError:
        print("PAGE NOT FOUND")
        break
