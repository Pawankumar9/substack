import requests
from bs4 import BeautifulSoup

url = "https://crt.sh/?q=%.garena.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"}

r = requests.get(url, headers=headers)

content = r.text
soup = BeautifulSoup(content, "html5lib")

for i in soup.find_all("td", attrs={"style":False, "href":False}):
	try:
		print i.string
	except:
		pass