# 학교 홈페이지 공지사항 데이터 수집
# (셀리니엄 패키지를 활용하기 때문에 가능하면 초기 화면부터 진입하기!

# 순서
# 1. 앞에 느낌표 있는 공지사항 제외하고 숫자가 있는 일반 공지사항만 수집하기 [if-else문 사용]
#    (번호 / 제목 / 작성일 / 조회수)
# 2. 페이지 넘기면서 10페이지까지 데이터 수집하기. (리스트 개념을 활용한 방식 이용하기)
# 3. 오류 있는지 확인하기 및 액셀파일로 저장하기.

from selenium import webdriver
import openpyxl
import time

# 웹드라이브 켜기 / 액셀파일 생성
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["번호", "제목", "작성일", "조회수"])
driver = webdriver.Chrome("./chromedriver")

# 학교 웹사이트 접속하기
driver.get("https://www.mju.ac.kr/mjukr/255/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGbWp1a3IlMkYxNDElMkZhcnRjbExpc3QuZG8lM0Y%3D")
time.sleep(4)


# 반복문 구조를 생각하며 여러 페이지 데이터 수집하기
for n in range(1, 11) :
    time.sleep(3)
    infobox1 = driver.find_elements_by_css_selector("tr._artclEven")
    infobox2 = driver.find_elements_by_css_selector("tr._artclOdd")
    for info in infobox1 :
        num = info.find_element_by_css_selector("td._artclTdNum").text
        if num == "일반공지" :
            continue
        tit = info.find_element_by_css_selector("td._artclTdTitle").text
        dat = info.find_element_by_css_selector("td._artclTdRdate").text
        vnum = info.find_element_by_css_selector("td._artclTdAccess").text
        print(num, "|", tit, "|", dat, "|", vnum)
        sheet.append([num, tit, dat, vnum])
    for info in infobox2 :
        num = info.find_element_by_css_selector("td._artclTdNum").text
        if num == "일반공지" :
            continue
        tit = info.find_element_by_css_selector("td._artclTdTitle").text
        dat = info.find_element_by_css_selector("td._artclTdRdate").text
        vnum = info.find_element_by_css_selector("td._artclTdAccess").text
        print(num, "|", tit, "|", dat, "|", vnum)
        sheet.append([num, tit, dat, vnum])

    page_bar = driver.find_elements_by_css_selector("div._inner ul > *")
    if n%10 != 0 :
        page_bar[n%10-1].click()
    else :
        next_B = driver.find_element_by_css_selector("a._next")
        next_B.click()

## 선택자
## 컨테이너 : tr._artclEven
## 번호 : td._artclTdNum
## 제목 : td._artclTdTitle
## 작성일 : td._artclTdRdate
## 조회수 : td._artclTdAccess

## 페이지 bar : div._inner

## 출력/액셀파일에 데이터 저장
#크롬창 닫기
driver.close()
#액셀파일 저장
wb.save("school_info.xlsx")