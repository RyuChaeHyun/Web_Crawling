from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver.exe")
#2. 파파고 접속하기
driver.get("https://papago.naver.com/")

time.sleep(1)
#3. 검색창에 검색어 입력하기 // 검색창 : textarea#txtSource
inter = driver.find_element_by_css_selector("textarea#txtSource")
inter.send_keys("Seize the day")

driver.implicitly_wait(10)

#4. 검색버튼 누르기 // 검색버튼:button#btnTranslate
search_button = driver.find_element_by_css_selector("button#btnTranslate")
driver.execute_script("arguments[0].click();", search_button)
# search_button.click()

time.sleep(1)
# papago = driver.find_elements_by_css_selector("div.rwd_box___1ysJh")

papago = driver.find_element_by_css_selector("div#txtTarget").text
print(papago)