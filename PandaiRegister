from selenium import webdriver
driver = webdriver.Chrome
driver = webdriver.Chrome("C:\\chromedriver")

driver.get("https://testv2.pandai.cn")
driver.find_element_by_class_name("border-radius").click()

driver.get("https://testv2.pandai.cn/registers/new")
driver.find_element_by_id("username").send_keys(18614234954)
driver.find_element_by_id("verification").send_keys("0000")
driver.find_element_by_id("invitationcode").send_keys("0000")

driver.find_element_by_id("checkbox").click()
#driver.find_element_by_id("checkbox").click()
driver.find_element_by_id("submit").click()

