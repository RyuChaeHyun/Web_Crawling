from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver.exe")
#2. 네이버 웹툰 접속하기
driver.get("https://series.naver.com/comic/top100List.nhn")

time.sleep(1)

driver.implicitly_wait(10)

n=2
for n in range(5):
    time.sleep(3)
    #컨테이너
    comic = driver.find_elements_by_css_selector("div.comic_cont")

    #제목,작가,별점,예고
    driver.implicitly_wait(3)

    for s in comic:
        # try:
        name = s.find_element_by_css_selector("h3>a").text
        # except:
        #     name = "제목이 없습니다"
        # try:
        writer = s.find_element_by_css_selector("span.ellipsis")
        # except:
        #     writer="작가가 없습니다"
        # try:
        star = s.find_element_by_css_selector("em.score_num").text
        # except:
        #     star="평점이 없습니다"
        # try:
        player = s.find_element_by_css_selector("p.dsc").text
        # except:
        #     player="예고가 없습니다"

        print(name)
        print(writer.text)
        print(star)
        print(player)

    driver.implicitly_wait(10)
    next_button = driver.find_element_by_css_selector("div.pagenate.paginate_v2 a")

    try:
        if n%5 !=0:
            next_button[n%5 + 1].click()
        else:
             driver.execute_script("arguments[2].click();", next_button)
    except:
        print("수집완료")




