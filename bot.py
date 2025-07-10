from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome seçenekleri
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")  # Ekransız mod

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.sahibinden.com/")  # Örnek URL, istediğin sayfayı yazabilirsin
    print(driver.title)

    # Buraya fırsat ilanları kontrol ve mesaj gönderme logic'i eklenir
    time.sleep(5)

finally:
    driver.quit()
