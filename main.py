from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
import time

# Local path to chrome driver
chrome_driver_path = Service("YOUR_PATH_TO_DRIVER")

driver = webdriver.Chrome(service=chrome_driver_path, options=webdriver.ChromeOptions())

driver.get("http://orteil.dashnet.org/experiments/cookie/")

def upgrade():
    buy_list = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    buy_list.reverse()
    for item in buy_list:
        if item.value_of_css_property("color") != "rgba(255, 0, 0, 1)":
            try:
                item.click()
            except StaleElementReferenceException:
                pass
            break


cookie = driver.find_element(By.ID, "cookie")
timeout = time.time() + 60 * 5
counter = 0

while True:
    time.sleep(0.001)
    cookie.click()
    counter += 0.075
    if counter > 30:
        upgrade()
        counter = 0
    if time.time() > timeout:
        score = driver.find_element(By.ID, "cps")
        print(score.text)
        break
