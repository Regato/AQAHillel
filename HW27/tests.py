from time import sleep

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


main_url = "https://www.python.org/"
applications_url = "about/apps/"


service = Service("./chromedriver")
chrome = Chrome(service=service)
action = ActionChains(chrome)
chrome.maximize_window()


chrome.get(url=main_url)
sleep(5)

try:
    assert chrome.current_url == main_url
except AssertionError:
    print(f"Assertion failed. Actual value is {chrome.current_url}")


about_button = chrome.find_element(by=By.ID, value="about")
action.move_to_element(about_button)
action.perform()
sleep(3)


applications_button = chrome.find_element(by=By.XPATH, value=f"//a[@href=\"/{applications_url}\"]")
applications_button.click()
sleep(5)

check_title = "Applications for Python | Python.org"

try:
    assert chrome.title == check_title
except AssertionError:
    print(f"Assertion failed. Actual value is {chrome.title}")

try:
    assert chrome.current_url == main_url + applications_url
except AssertionError:
    print(f"Assertion failed. Actual value is {chrome.current_url}")


chrome.close()
