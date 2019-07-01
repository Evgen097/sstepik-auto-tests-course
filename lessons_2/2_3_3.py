
#	Открыть страницу http://suninjuly.github.io/alert_accept.html
#	Нажать на кнопку
#	Принять confirm
#	На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(1)
alert = browser.switch_to.alert
alert.accept()
time.sleep(1)

x = browser.find_element_by_id("input_value").text

y = calc(x)

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)

time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")

button.click()














