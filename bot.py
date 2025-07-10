from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--headless=new")  # İstersen headless kaldır (penceresiz çalışır)

driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)

try:
    driver.get("https://web.whatsapp.com")
    print("QR kodu okut, sonra Enter’a bas.")
    input()

    # Alıcı kişinin adı (telefon rehberinde nasıl kayıtlıysa)
    target_name = "Onur"

    # Gönderilecek mesaj
    message = "Merhaba! Bu mesaj otomatik gönderildi 🤖"

    # Kişinin sohbetini bul
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
    search_box.click()
    search_box.send_keys(target_name)
    time.sleep(2)

    user = driver.find_element(By.XPATH, f"//span[@title='{target_name}']")
    user.click()

    # Mesaj kutusunu bul
    message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
    message_box.send_keys(message)

    # Gönder butonuna tıkla
    send_button = driver.find_element(By.XPATH, "//button[@data-testid='compose-btn-send']")
    send_button.click()

    print("Mesaj başarıyla gönderildi!")

except Exception as e:
    print("Hata:", e)

finally:
    driver.quit()
