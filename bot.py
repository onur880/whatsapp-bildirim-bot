from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome seçeneklerini ayarla
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"
# chrome_options.add_argument("--headless")  # Bunu kapalı bıraktık (başına # koyduk)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Chrome driver servisini ayarla
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test için Google'a git
driver.get("https://www.google.com")
print(driver.title)

driver.quit()
