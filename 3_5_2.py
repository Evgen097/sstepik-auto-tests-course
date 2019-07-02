
чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip:

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):

    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
		
		
		
Чтобы увидеть это сообщение в консоли,
при запуске нужно добавлять параметр pytest -rsx. 
class TestMainPage1(object):

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_guest_should_see_login_link(self, browser):		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		