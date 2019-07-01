from selenium import webdriver

browser = webdriver.Chrome()
browser.get(link)


browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(1)").click()

browser.find_element_by_css_selector("[value='1']").click()

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"


Можно использовать еще два метода: select.select_by_visible_text("text")
 и select.select_by_index(index). 
 Первый способ ищет элемент по видимому тексту, например, 
 select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

Второй способ ищет элемент по его индексу или порядковому номеру.
 Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python", 
 нужно использовать select.select_by_index(1),
 так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".



