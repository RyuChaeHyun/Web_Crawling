import requests
from bs4 import BeautifulSoup

for page in range(1,52,50) :
    raw = requests.get("https://www.melon.com/chart/index.htm#params%5Bidx%5D=" + str(page),
                       headers = {"User-Agent" : "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 1. 컨테이너 :  tr.lst50
    # 2. 노래 제목 : div.wrap_song_info span a
    # 3. 아티스트 : div.ellipsis.rank02 a
    # 4. 수록앨범 : div.ellipsis.rank03 a

    containers = html.select("tr.lst50")

    # 기사 데이터 수집
    for cont in containers:
        title = cont.select_one("div.wrap_song_info span a").text
        artist = cont.select_one("div.ellipsis.rank02 a").text
        album = cont.select_one("div.ellipsis.rank03 a").text

        print(title)
        print(artist)
        print(album)

        print("*" * 50)