import time
import math

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    #link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    answer = math.log(int(time.time()))
    time.sleep(5)
    answer = str(answer)
    area = browser.find_element_by_tag_name("textarea")
    print(area)
    area.send_keys(answer)
    btn = browser.find_element_by_class_name("submit-submission")
    btn.click()
    time.sleep(5)
    msg = browser.find_element_by_class_name("smart-hints__hint")
    assert "Correct!" in msg.text, "Тест завершён не корректно"
    
