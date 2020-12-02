from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/math.html"
	browser.get(link)

	num = browser.find_element_by_id("input_value").text
	sum = math.log(abs(12*math.sin(int(num))))


	input = browser.find_element_by_id("answer")
	input.send_keys(str(sum)) 

	checkbox1 = browser.find_element_by_id("robotCheckbox")
	checkbox1.click()
	
	radiobatton1 = browser.find_element_by_id("robotsRule")
	radiobatton1.click()
	
	button = browser.find_element_by_class_name("btn.btn-default")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()