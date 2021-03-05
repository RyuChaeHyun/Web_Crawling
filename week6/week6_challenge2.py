from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver.exe")
#2. 파파고 접속하기
driver.get("https://www.google.com/maps")

time.sleep(1)
inter = driver.find_element_by_css_selector("input#searchboxinput")
inter.send_keys("카페")

driver.implicitly_wait(10)

search_button = driver.find_element_by_css_selector("button#searchbox-searchbutton")
driver.execute_script("arguments[0].click();", search_button)
# search_button.click()

for n in range(10):
    time.sleep(3)
    #컨테이너
    cafe = driver.find_elements_by_css_selector("div.section-result-content")

    #평점
    #주소
    driver.implicitly_wait(20)

    for s in cafe:
        try:
            name = s.find_element_by_css_selector("h3>span").text
        except:
            name = "이름이 없습니다"
        try:
            star = s.find_element_by_css_selector("span.cards-rating-score").text
        except:
            star="평점이 없습니다"

        print(name)
        print(star)

    driver.implicitly_wait(10)

    try:
        next_button = driver.find_element_by_css_selector("span.n7lv7yjyC35__button-next-icon")
        driver.execute_script("arguments[0].click();", next_button)
    except:
        print("수집완료")
        break

