from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url = 'https://www.tokopedia.com/msi-id/review'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(url)

data = []

for i in range (0, 3):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.findAll('article', attrs = {'class':'css-a21zsk'})
    for container in containers:
        try:
            review = container.find('span', attrs = {'data-testid':'lblItemUlasan'}).text
            data.append(
            (review)
            )
        except AttributeError: 
            continue

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
    time.sleep(3)

print(data)