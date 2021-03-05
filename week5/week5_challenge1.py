import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/list/ls016522954/",
                   headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너 div.lister-item-content
movies = html.select("div.lister-item-content")

# 제목 h3>a
# 장르 span.genre
# 감독  p.text-muted>a
# 배우 p.text-muted>a

for m in movies:
    title = m.select_one("h3>a").text
    genre = m.select_one("span.genre").text

    try:
        # # select 함수를 이용하는 방법
        info = m.select("p.text-muted")
        # # 감독
        director = info[1].select("a")
        # # 배우
        actor = info[2].select("a")

        if "Action" not in genre:
            continue

        print(title)
        print(genre)
        for d in director:
            print(d.text)
        for a in actor:
            print(a.text)

        print("*" * 50)
    except:
        print("감독 또는 배우가 없습니다")
