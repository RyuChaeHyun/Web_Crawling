import requests
from bs4 import BeautifulSoup

raw = requests.get("https://v4.map.naver.com/",
                headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너 div.lsnx
stores = html.select("div.lsnx")
print(stores)
#가게이름
#가게주소
#전화번호