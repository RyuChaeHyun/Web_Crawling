import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("https://www.imdb.com/list/ls016522954/",
                   headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너 div.lister-item-content
movies = html.select("div.lister-item")

# 제목 h3>a
# 장르 span.genre
# 감독  p.text-muted>a
# 배우 p.text-muted>a

for m in movies:
    title = m.select_one("h3>a")
    url = title.attrs["href"]
    print("*"*50)
    print(title.text)

    each_raw = requests.get("https://www.imdb.com/list/ls016522954/" + url,
                            headers={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    poster =  each_html.select_one("div.slate_wrapper div.poster img")
    poster_src = poster.attrs["src"]
    urlretrieve(poster_src, "poster/" + title.text[:3] + ".png")
