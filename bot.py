import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--remote-debugging-port=9222")

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.sahibinden.com/alfa-romeo")
    time.sleep(5)

    ilanlar = driver.find_elements(By.CSS_SELECTOR, ".searchResultsRowClass")
    for ilan in ilanlar[:5]:  # İlk 5 ilanı örnek yazdır
        baslik = ilan.find_element(By.CSS_SELECTOR, ".searchResultsTitleValue").text
        fiyat = ilan.find_element(By.CSS_SELECTOR, ".searchResultsPriceValue").text
        print("Başlık:", baslik)
        print("Fiyat:", fiyat)
        print("-----")

finally:
    driver.quit()
