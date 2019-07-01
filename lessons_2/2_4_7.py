
#	Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#	Дождаться, когда цена дома уменьшится до 10000 RUR 
#	(ожидание нужно установить не меньше 12 секунд)
#
#	Нажать на кнопку "Забронировать"
#
#	Решить уже известную нам математическую задачу 
#	(используйте ранее написанный код) и отправить решение


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)


browser.get("http://suninjuly.github.io/explicit_wait2.html")
time.sleep(5)
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "1000"))

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

x = browser.find_element_by_id("input_value").text
y = calc(x)

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)


buttons = browser.find_element_by_id("solve")
buttons.click()































