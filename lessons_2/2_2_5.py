import time
from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

time.sleep(3)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(3)

browser.execute_script("window.scrollBy(0, 100);")
time.sleep(3)

browser.execute_script("window.scrollBy(0, 100);")
time.sleep(3)

button.click()



option2 = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
time.sleep(1)
option2.click()

time.sleep(1)
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

button.click()














