from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")

id = driver.find_element_by_css_selector("input#id.tf_g")
id.send_keys("lch010201")

password = driver.find_element_by_css_selector("input#inputPwd.tf_g")
password.send_keys("lch6683!")


search_button = driver.find_element_by_css_selector("button#loginBtn.btn_comm")
driver.execute_script("arguments[0].click();", search_button)
# search_button.click()

