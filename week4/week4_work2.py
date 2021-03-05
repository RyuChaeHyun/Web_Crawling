import requests
from bs4 import BeautifulSoup
import openpyxl

# f = open("navertv.csv", "w", encoding='UTF-8')
# f.write("아티스트, 제목, 수록 앨범\n")

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["아티스트", "제목", "수록 앨범"])

for page in range(1,10):
    raw = requests.get("https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200512&hh=18&rtm=Y&pg="+str(page),
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너: tr.list
#아티스트: a.artist.ellipsis
#제목: a.title.ellipsis
#수록앨범: a.albumtitle.ellipsis

    containers = html.select("tr.list")

    # 기사 데이터 수집
    for cont in containers:
        artist = cont.select_one("a.artist.ellipsis").text.strip()
        title = cont.select_one("a.title.ellipsis").text.strip()
        album = cont.select_one("a.albumtitle.ellipsis").text.strip()

        artist = artist.replace(",", "")
        title = title.replace(",", "")
        album = album.replace(",", "")

        print(artist, title, album)
#         print(artist + "," + title + "," + albumtitle)
#         f.write(artist + "," + title + "," + + album + "\n")
#
# f.close()
        sheet.append([artist, title, album])

wb.save("genie.xlsx")
