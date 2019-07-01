
#	Открыть страницу http://suninjuly.github.io/redirect_accept.html
#	Нажать на кнопку
#	Переключиться на новую вкладку
#	Пройти капчу для робота и получить число-ответ

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
 

#	browser.switch_to.window(window_name)
#	new_window = browser.window_handles[1]
#	first_window = browser.window_handles[0]
#	current_window = browser.current_window_handle



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)

# Отправляем заполненную форму
x = browser.find_element_by_id("input_value").text
y = calc(x)

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)

time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")

button.click()














