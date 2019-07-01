
#	Открыть страницу http://suninjuly.github.io/file_input.html
#	Заполнить текстовые поля: имя, фамилия, email
#	Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#	Нажать кнопку "Отправить"

from selenium import webdriver
import time
import math

import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_css_selector("[name='firstname']")
input1.send_keys("Ivan")


input2 = browser.find_element_by_css_selector("[name='lastname']")
input2.send_keys("Petrov")


input3 = browser.find_element_by_css_selector("[name='email']")
input3.send_keys("myemail@gmail.com")



inputf = browser.find_element_by_css_selector("#file")
inputf.send_keys(file_path)





time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")

button.click()
















