import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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


MAILHOST = ""
USERNAME = ""
PASSWORD = ""  
SEND_FROM = ""
SEND_FROM_NAME = ""
REPLY_TO = ""
REPLY_TO_NAME = ""
to_email = input("E-posta gönderilecek adresi giriniz: ")

adet = int(input("Kaç ürün kontrol etmek istiyorsunuz? "))
beden = input("Kontrol edilmesini istediğiniz bedeni giriniz: ")
linkler = []
for i in range(adet):
    link = input(f"{i+1}. Link giriniz: ")
    linkler.append(link)

def send_email(subject, body):
    # E-posta içeriği oluşturma
    msg = MIMEMultipart()
    msg['From'] = SEND_FROM
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    msg['Reply-To'] = f"{REPLY_TO_NAME} <{REPLY_TO}>"

    try:
        # SMTP sunucusuna bağlanma
        server = smtplib.SMTP(MAILHOST, 587)
        server.starttls()  
        server.login(USERNAME, PASSWORD) 
        text = msg.as_string()
        server.sendmail(SEND_FROM, to_email, text) 
        server.quit()  
        print("E-posta gönderildi.")
    except Exception as e:
        print(f"E-posta gönderme hatası: {e}")

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
                    winsound.Beep(1000, 1000)  # Sesli uyarı
                    send_email("Ürün Bulundu!", f"Kriterlere uygun bir ürün bulundu: {link}")
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
