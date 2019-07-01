from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#Открыть страницу http://suninjuly.github.io/math.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x (код для этого приведён ниже).
#Ввести ответ в текстовое поле.
#Отметить checkbox "Подтверждаю, что являюсь роботом".
#Выбрать radiobutton "Роботы рулят!".
#Нажать на кнопку Отправить.

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

human_radio = browser.find_element_by_id("humanRule")
human_checked = human_radio.get_attribute("checked")
print("value of human radio: ", human_checked)
assert human_checked is not None, "Human radio is not selected by default"

assert human_checked == "true", "Human radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()












	