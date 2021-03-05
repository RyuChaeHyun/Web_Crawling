import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "기사 요약"])

for page in range(1,4) :
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&&cluster_page=" + str(page))
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너 :ul#clusterResultUL>li
    # 제목 :div.wrap_tit
    # 기사요약 :p.f_eb

    # 컨테이너 수집
    containers = html.select("ul#clusterResultUL>li")

    # 기사 데이터 수집
    for cont in containers:
        title = cont.select_one("div.wrap_tit").text
        summary = cont.select_one("p.f_eb").text

        print(title, summary)

        sheet.append([title,summary])

wb.save("summaryar.xlsx")