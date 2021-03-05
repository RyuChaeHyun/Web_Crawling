import requests
from bs4 import BeautifulSoup

# csv 형식으로 저장하기
f = open("navertv.csv", "w", encoding='UTF-8')
f.write("제목, 채널명, 채널수, 좋아요\n")

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text, 'html.parser')

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
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    title = title.replace("," ,"")
    chn = chn.replace("," ,"")
    hit = hit.replace("," ,"")
    like = like.replace("," ,"")

    hit = hit.replace("재생 수", "")
    like = like[5:]

    # print(title)
    # print(chn)
    # print(hit)
    # print(like)
    # print("=" * 50)
    f.write(title+","+chn+ "," + hit+"," + like + "\n")

f.close()
