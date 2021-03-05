#셀레니움 연습하기
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.daum.net/")

cafe_button = driver.find_element_by_css_selector("a.txt_pctop.link_cafe")
driver.execute_script("arguments[0].click();", cafe_button)

#5. 검색 결과 확인하기

n=1
for n in range(1,11):
    #지연 시간 추가
    time.sleep(1)
    stores = driver.find_elements_by_css_selector("a.link_popular")

    driver.implicitly_wait(1)

    for s in stores:
        try:
           number = s.find_element_by_css_selector("span.num_item").text
        except:
            number="광고"
        try:
            title = s.find_element_by_css_selector("p.desc_info").text
        except:
            title = "제목이 없습니다"
        try:
            addr = s.find_element_by_css_selector("span.txt_item").text
        except:
            addr="주소가 없습니다"
        print(number)
        print(title)
        print(addr)
    driver.implicitly_wait(1)

    # 페이지버튼 div.paginate > *
    try:
        next_button = driver.find_element_by_css_selector("button.btn_item.btn_next")
        driver.execute_script("arguments[0].click();", next_button)
    except:
        print("수집완료")

driver.close()
