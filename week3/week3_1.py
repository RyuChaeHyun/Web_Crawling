import requests
from bs4 import BeautifulSoup
#beautifulsoup4 bs4 파일안에 있고 beautifulsoup 이라는 기능 사용할 것!

raw = requests.get("https://tv.naver.com/r/")
#print(raw)
#print(raw.text)
#print(raw.elapsed)

html = BeautifulSoup(raw.text, 'html.parser')
#print(html)

# 1-3위 컨테이너: div.inner
# 제목 :  dt.title
# 채널명 : dd.chn
# 재생수 : span.hit
# 좋아요수 : span.like

#1. 컨테이너 수집
container = html.select("div.inner")
# print(container[0])

#2. 영상데이터 수집
for cont in container :
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("=" * 50)

#3. 반복하기

# 4-100위 컨테이너: div.cds_type
# 제목 :  dt.title
# 채널명 : dd.chn
# 재생수 : span.hit
# 좋아요수 : span.like
container2 = html.select("div.cds_type")

for cont in container2 :
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("=" * 50)

