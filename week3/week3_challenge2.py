import requests
from bs4 import BeautifulSoup

for page in range(1,10,1):
    raw = requests.get("https://news.ycombinator.com/news?p="+str(page),
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너 : tr.athing
    # 순위 : span.rank
    # 제목 : a.storylink

    #1. 컨테이너 수집
    containers = html.select("tr.athing")

    #2. 기사 데이터 수집
    for cont in containers :
        rank = cont.select_one("span.rank").text
        title = cont.select_one("a.storylink").text

        print(rank, title)

#3. 반복하기