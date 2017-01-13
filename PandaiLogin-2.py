from selenium import webdriver
driver = webdriver.Chrome
driver = webdriver.Chrome("C:\\chromedriver")

driver.get("https://testv2.pandai.cn")

driver.find_element_by_link_text("登录").click()

driver.get("https://testv2.pandai.cn/sessions/new#")

driver.find_element_by_id("login").clear()
driver.find_element_by_id("login").send_keys("18611173913")
driver.find_element_by_id("password").send_keys("test123")
#driver.find_element_by_id("vcode").send_keys("0000")
driver.find_element_by_name("commit").click()

driver.implicitly_wait(5)

name = driver.find_element_by_class_name("lender_login").text
#name1 = str(name)
if "34324234234" in name:
    print("true")
else:
    print("false")

driver.quit()

#result = driver.find_element_by_id("login-form").text
#print (result)
