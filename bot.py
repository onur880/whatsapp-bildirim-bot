from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome seçeneklerini ayarlıyoruz
chrome_options = Options()
chrome_options.add_argument("--headless")             # Arka planda çalıştır
chrome_options.add_argument("--no-sandbox")           # Sandbox kapalı
chrome_options.add_argument("--disable-dev-shm-usage")# /dev/shm sorunlarını çöz
chrome_options.add_argument("--disable-gpu")          # GPU devre dışı
chrome_options.add_argument("--remote-debugging-port=9222")  # Debug portu

# ChromeDriver yolu
service = Service('/usr/bin/chromedriver')

# Sürücüyü başlat
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test için bir sayfaya git
driver.get("https://www.google.com")
print("Sayfa başlığı:", driver.title)

# Biraz bekle
time.sleep(3)

# Tarayıcıyı kapat
driver.quit()
