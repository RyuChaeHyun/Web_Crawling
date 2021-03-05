import requests
from bs4 import BeautifulSoup

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx",
                   headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

movies = html.select("ul.list_boxthumb > li")

for m in movies:

    #제목
    title = m.select_one("strong.tit_join>a")
    url = title.attrs["href"]
    #상세페이지
    each_raw = requests.get(url,
                            headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    title = each_html.select_one("strong.tit_movie").text
    score = each_html.select_one("em.emph_grade").text



    genre = each_html.select_one("dl.list_movie>dd:nth-of-type(1)").text
    director = each_html.select("dl.list_movie>dd:nth-of-type(5) a")
    actor = each_html.select("dl.list_movie>dd:nth-of-type(6) a")

    print("제목 : ", title)
    print("평점 : ", score)
    print("장르 : ", genre)


    for d in director:
        print(d.text)

    for a in actor:
        print(a.text)

    print("=" * 50)