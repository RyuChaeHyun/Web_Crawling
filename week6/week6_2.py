#셀레니움 연습하기
from selenium import webdriver
import time

#1. 웹 드라이버 켜지
driver = webdriver.Chrome("./chromedriver.exe")
#2. 네이버 지도 접속하기
driver.get("https://v4.map.naver.com/")
#3. 검색창에 검색어 입력하기 // 검색창 : input#search-input
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")
#4. 검색버튼 누르기 // 검색버튼:button.spm
search_button = driver.find_element_by_css_selector("button.spm")
driver.execute_script("arguments[0].click();", search_button)
# search_button.click()

#5. 검색 결과 확인하기

n=1
for n in range(1,20):
    #지연 시간 추가
    time.sleep(1)

    #컨테이너 div.lsnx
    #가게이름  dt>a
    #가게주소 dd.addr
    #전화번호 dd.tel

    # stores = html.select("div.lsnx")
    ## 여러가지 데이터 리스트 형식으로 받음
    stores = driver.find_elements_by_css_selector("div.lsnx")

    for s in stores:
        name = s.find_element_by_css_selector("dt>a").text
        addr = s.find_element_by_css_selector("dd.addr").text
        try:
            tel = s.find_element_by_css_selector("dd.tel").text
        except:
            tel="전화번호 없음"
        print(name)
        print(addr)
        print(tel)

    # 페이지버튼 div.paginate > *
    page_bar = driver.find_element_by_css_selector("div.paginate>*")

    try:
        if n%5 !=0:
            page_bar[n%5 + 1].click()
        else:
            page_bar[6].click()
            driver.execute_script("arguments[2].click();", page_bar)
    except:
        print("수집완료")
        break

