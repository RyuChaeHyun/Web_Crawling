import requests
from bs4 import BeautifulSoup

for page in range(1, 6) :
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page=" + str(page),
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    #컨테이너 :ul.lst_thum_wrap li
    #제목 :a strong
    #저자 :a span.writer

    # 컨테이너 수집
    containers = html.select("div.lst_thum_wrap li")

    #기사 데이터 수집
    for cont in containers :
        title = cont.select_one("a strong").text
        writer = cont.select_one("span.writer").text

        print(title,writer)