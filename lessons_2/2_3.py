from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
#	Открыть страницу http://suninjuly.github.io/get_attribute.html.
#	Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#	Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#	Посчитать математическую функцию от x (сама функция остаётся неизменной).
#	Ввести ответ в текстовое поле.
#	Отметить checkbox "Подтверждаю, что являюсь роботом".
#	Выбрать radiobutton "Роботы рулят!".
#	Нажать на кнопку "Отправить".

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_id("treasure")
treasure_valuex = treasure.get_attribute("valuex")

y = calc(treasure_valuex)


input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)


option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()


option1 = browser.find_element_by_css_selector("#robotsRule")
option1.click()


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()














	