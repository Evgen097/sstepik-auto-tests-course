
#	Открыть страницу http://suninjuly.github.io/selects1.html
#	Посчитать сумму заданных чисел
#	Выбрать в выпадающем списке значение равное расчитанной сумме
#	Нажать кнопку "Отправить"


from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"
browser.get(link)


browser.execute_script("alert('Robots at work');")

browser.execute_script("document.title='Script executing';alert('Robots at work');")

Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
element = browser.execute_script('document.getElementsByName("name")')

Так же есть конструкции:
getElementById
getElementsByTagName
getElementsByClassName
querySelector - для CSS
querySelectorAll - для CSS (находит все совпадения)

evaluate - для XPATH.

# Отправляем заполненную форму
#button = browser.find_element_by_css_selector("button.btn")
#button.click()

















