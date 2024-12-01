import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import winsound 

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-blink-features")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

adet = int(input("Kaç ürün kontrol etmek istiyorsunuz? "))
beden = input("Kontrol edilmesini istediğiniz bedeni giriniz: ")
linkler = []
for i in range(adet):
    link = input(f"{i+1}. Link giriniz: ")
    linkler.append(link)

try:
    while True:  
        for link in linkler:
            driver.get(link)
            print(f"\nZiyaret edilen link: {link}")
            try:
                li_elements = driver.find_elements(By.CLASS_NAME, "size-selector-sizes-size__button")
                found = False

                for li in li_elements:
                    size_info = li.find_element(By.CLASS_NAME, "size-selector-sizes-size__info")
                    has_availability = size_info.find_elements(By.CLASS_NAME, "size-selector-sizes-size__availability")
                    has_view_similars = size_info.find_elements(By.CLASS_NAME, "size-selector-sizes-size__view-similars")

                    if not has_availability and not has_view_similars:
                        size_label = li.find_element(By.CLASS_NAME, "size-selector-sizes-size__label").text.strip()
                        if size_label == f"{beden} (US {beden})":
                            found = True
                            break

                if found:
                    print("Kriterlere uyan bir ürün bulundu!")
                    winsound.Beep(1000, 1000)
                else:
                    print("Kriterlere uyan bir ürün bulunamadı.")

            except Exception as e:
                print(f"Kontrol sırasında bir hata oluştu: {e}")

        print("\n30 saniye sonra tekrar kontrol edilecek...")
        time.sleep(30)

except KeyboardInterrupt:
    print("\nUygulama sonlandırılıyor...")
finally:
    driver.quit()
