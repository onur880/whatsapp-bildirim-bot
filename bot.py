from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Tarayıcıyı başlat
service = Service('/usr/bin/chromedriver')  # Sunucundaki chromedriver yolu, gerekirse güncelle
driver = webdriver.Chrome(service=service)

# WhatsApp Web'e git
driver.get("https://web.whatsapp.com")
print("QR kodu okut ve Enter'a bas...") 
input()  # QR kodu okutmak için bekler

# Mesaj göndermek istediğin kişi adı
target_name = "KimeMesajAtacaksan"

# Mesaj içeriği
message = "Merhaba! Bu bir test mesajıdır."

# Kişiyi bul
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(target_name)
time.sleep(2)

# Kişiyi seç
user = driver.find_element(By.XPATH, f'//span[@title="{target_name}"]')
user.click()

# Mesaj kutusunu bul
message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
message_box.click()
message_box.send_keys(message)

# Gönder butonuna bas
send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
send_button.click()

print("Mesaj gönderildi!")

# Tarayıcıyı kapatma (test için açık kalsın)
# driver.quit()
