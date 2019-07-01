import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

try:

	link = "http://suninjuly.github.io/simple_form_find_task.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_tag_name("input")
	input1.send_keys("Ivan")


	input2 = browser.find_element_by_name("last_name")
	input2.send_keys("Petrov")


	input3 = browser.find_element_by_class_name("city")
	input3.send_keys("Smolensk")


	input4 = browser.find_element_by_id("country")
	input4.send_keys("Russia")


	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	
	time.sleep(1)

	
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    browser.close()
    time.sleep(2)
    browser.quit()
	