from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
print(driver.title)

driver.quit()
