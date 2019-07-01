
#	Открыть страницу http://suninjuly.github.io/selects1.html
#	Посчитать сумму заданных чисел
#	Выбрать в выпадающем списке значение равное расчитанной сумме
#	Нажать кнопку "Отправить"


from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"
browser.get(link)

num1 = browser.find_element_by_css_selector("#num1")
num2 = browser.find_element_by_css_selector("#num2")

y = str(int(num1.text) + int(num2.text))

browser.find_element_by_tag_name("select").click()

browser.find_element_by_css_selector("[value='" + y + "']").click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

















