from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome seçenekleri
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--headless=new")  # <<< EN ÖNEMLİ

# ChromeDriver servisi
service = Service("/usr/bin/chromedriver")

# Tarayıcıyı başlat
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test için Google'a git
driver.get("https://www.google.com")

# Sayfa başlığını yazdır
print(driver.title)

# Tarayıcıyı kapat
driver.quit()
