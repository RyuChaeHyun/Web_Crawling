import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers = {"User-Agent" : "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 복습과제1
# 1. 컨테이너 : ul.lst_detail_t1 li
# 2. 영화제목 : li dt.tit a
# 3. 평점 :div.star_t1 span.num
# 4. 예매율 : dl.info_exp span.num

containers = html.select("ul.lst_detail_t1 li")

for cont in containers :
    title = cont.select_one("li dt.tit a").text
    score = cont.select_one("div.star_t1 span.num").text
    percent = cont.select_one("dl.info_exp span.num").text

    print(title)
    print(score)
    print(percent)
    print("^"*50)
