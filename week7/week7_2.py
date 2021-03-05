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

inter = driver.find_element_by_css_selector("tr._artclEven td._artclTdTitle")
# search_button.click()

for n in range(10):
    time.sleep(3)
    #컨테이너
    cont = driver.find_elements_by_css_selector("tr._artclOdd")

    #번호 / 제목 / 작성일 / 조회수
    driver.implicitly_wait(20)

    for s in cont:
        try:
            number = s.find_element_by_css_selector("td._artclTdNum").text
        except:
            number = "숫자가 없습니다"
        try:
            title = s.find_element_by_css_selector("a.artclLinkView").text
        except:
            title="평점이 없습니다"
        try:
            date = s.find_element_by_css_selector("td._artclTdWriter").text
        except:
            date = "평점이 없습니다"
        try:
            sum = s.find_element_by_css_selector("td._artclTdAccess").text
        except:
            sum = "평점이 없습니다"

        print(number)
        print(title)
        print(date)
        print(sum)

    driver.implicitly_wait(10)

    try:
        next_button = driver.find_element_by_css_selector("div._inner ul > *")
        if n % 10 != 0:
            next_button[n % 10 - 1].click()
        else:
            next_B = driver.find_element_by_css_selector("a._next")
            next_B.click()

    except:
        print("수집완료")
        break

