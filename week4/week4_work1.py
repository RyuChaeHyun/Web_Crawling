import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["영화제목", "평점"])


raw = requests.get("https://movie.naver.com/movie/running/current.nhn#")
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너: dl.lst_dsc
# 영화 제목: dt.tit a
# 평점: dl.info_star span.num

movie = html.select("dl.lst_dsc")

for mov in movie:
    title = mov.select_one("dt.tit a").text
    num = mov.select_one("dl.info_star span.num").text
    print(title, num)

    sheet.append([title,num])

wb.save("navermovie.xlsx")