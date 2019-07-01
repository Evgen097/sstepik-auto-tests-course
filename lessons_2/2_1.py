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

# Ваш код, который заполняет обязательные поля
x = int(browser.find_element_by_css_selector("#input_value").text)
y = calc(x)

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)


option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()


option1 = browser.find_element_by_css_selector("#robotsRule")
option1.click()


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()












	