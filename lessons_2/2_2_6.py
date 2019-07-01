
#	Открыть страницу http://SunInJuly.github.io/execute_script.html.
#	Считать значение для переменной x.
#	Посчитать математическую функцию от x.
#	Проскроллить страницу вниз.
#	Ввести ответ в текстовое поле.
#	Выбрать checkbox "Подтверждаю, что являюсь роботом".
#	Переключить radiobutton "Роботы рулят!".
#	Нажать на кнопку "Отправить".

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)


x = browser.find_element_by_id("input_value").text
y = calc(x)


input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)


option1 = browser.find_element_by_css_selector("#robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()

time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")

button.click()
















