
selenium_env\Scripts\activate.bat 
(selenium_env) С:\Users\user\environments>  pip install pytest==3.10.1

pip freeze > requirements.txt
pip install -r requirements.txt


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

assert a == b, "Значения разные"
assert user_is_authorised(), "User is guest"

pytest -v test_abs.py

В этом шаге мы коротко обсудим важные особенности запуска тестов с помощью PyTest. Когда мы выполняем команду pytest, тест-раннер собирает все тесты для запуска по определенным правилам:
если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт поиск в текущей директории
как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов
дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории
во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  test_*.py или *_test.py (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py)
внутри всех этих файлов находит тестовые функции по следующему правилу:
все тесты, название которых начинается с test, которые находятся вне классов
все тесты, название которых начинается с test внутри классов, имя которых начинается с Test (и без метода __init__ внутри класса)
https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()

def test_exception():
    browser.get("https://mysite.com")
    with pytest.raises(NoSuchElementException, message="Не должно быть кнопки Отправить"):
        browser.find_element_by_css_selector("button.btn")



















