import math
import time

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    clicks = browser.find_elements_by_css_selector('.form-check-label')
    print(clicks)

    for clck in clicks:
        clck.click()

    btn = browser.find_element_by_css_selector('.btn')
    btn.click()

    # chbox = browser.find_element_by_css_selector('.form-check-input')
    # chbox.click()
    #
    # rbutton = browser.find_element_by_css_selector('.form-check-label')
    # rbutton.click()

# except Exception as e:
#     raise
finally:
    time.sleep(15)

    browser.quit()
