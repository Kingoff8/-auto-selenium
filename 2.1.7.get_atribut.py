import time
import math
from selenium import webdriver

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    img = browser.find_element_by_tag_name('img')
    x = img.get_attribute('valuex')
    print(x)
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    chbox = browser.find_element_by_id('robotCheckbox')
    chbox.click()

    rbutton = browser.find_element_by_id('robotsRule')
    rbutton.click()

    btn = browser.find_element_by_css_selector('.btn')
    btn.click()
    #print(img_attr)
finally:
    time.sleep(15)
    browser.quit()
