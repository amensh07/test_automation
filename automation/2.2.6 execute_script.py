import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    message_elt = browser.find_element_by_tag_name("h1")
    message = message_elt.text

    assert "Congrats" in message.text



finally:
    time.sleep(5)
    browser.quit()