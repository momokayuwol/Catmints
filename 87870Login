from selenium import webdriver
driver = webdriver.Chrome
driver = webdriver.Chrome("C:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python35-32\\chromedriver")

driver.get("http://www.87870.com/");

driver.find_element_by_id("login-pop").click()
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("momoka_yuwol")
driver.find_element_by_id("password").send_keys("loveyou2007")
#driver.find_element_by_id("vcode").send_keys("0000")
driver.find_element_by_id("lw-submit").click()

result = driver.find_element_by_id("login-widow").text
print (result)
