# подготовка для теста
import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
browser = webdriver.Chrome()
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
browser.get("https://fake-shop.com/book1.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# открываем страницу второго товара
browser.get("https://fake-shop.com/book2.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# тестовый сценарий
# открываем корзину
browser.get("https://fake-shop.com/basket.html")

# ищем все добавленные товары
goods = browser.find_elements_by_css_selector(".good")

# проверяем, что количество товаров равно 2
assert len(goods) == 2