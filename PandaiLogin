from selenium import webdriver
driver = webdriver.Chrome
driver = webdriver.Chrome("C:\\chromedriver")

driver.get("https://testv2.pandai.cn")

driver.find_element_by_link_text("登录").click()

driver.get("https://testv2.pandai.cn/sessions/new#")

driver.find_element_by_id("login").clear()
driver.find_element_by_id("login").send_keys("momoka_yuwol")
driver.find_element_by_id("password").send_keys("loveyou2007")
#driver.find_element_by_id("vcode").send_keys("0000")
driver.find_element_by_name("commit").click()

result = driver.find_element_by_id("login-form").text
print (result)
