import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 ul.lst_detail_t1 li

movies = html.select("ul.lst_detail_t1 li")

for m in movies:
    # 제목  dt.tit a
    # 이미지  div.thumb a img
    title = m.select_one("dt.tit a")
    image = m.select_one("div.thumb a img")
    print(title.text)

    image_src = image.attrs["src"]
    urlretrieve(image_src, "image/" + title.text[:2] + ".png")
