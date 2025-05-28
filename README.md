# 🐍 Python E-ticaret Ürün Stok ve Beden Takip Otomasyonu

![Python Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png)


Bu Python script'i, belirli e-ticaret sitelerindeki ürünlerin istediğiniz bedende stoğa girip girmediğini **otomatik olarak takip eder** ve ürün bulunduğunda sizi **e-posta ve sesli uyarı** ile bilgilendirir. Yoğun talep gören veya sınırlı sayıda üretilen ürünleri kaçırmak istemeyenler için ideal bir çözümdür!

Script, **Selenium WebDriver** kullanarak web sayfalarını dinamik olarak kontrol eder, sayfa yapısını analiz eder ve beden seçimi alanlarındaki stok durumunu inceler. `smtplib` kütüphanesi ile de profesyonel e-posta bildirimleri gönderir.

---

## 🌟 Temel Özellikler

*   **Çoklu Ürün Takibi:** Birden fazla ürün linkini aynı anda takip edebilme.
*   **Spesifik Beden Kontrolü:** Belirttiğiniz bedenin stok durumunu hassasiyetle kontrol etme.
*   **Periyodik Otomatik Kontrol:** Belirlenen aralıklarla (varsayılan 30 saniye) sürekli stok kontrolü.
*   **Anlık E-posta Bildirimi:** Ürün bulunduğunda, önceden tanımladığınız e-posta adresine bilgilendirme mesajı gönderme.
*   **Sesli Uyarı:** Ürün bulunduğunda `winsound` ile dikkat çekici bir sesli uyarı verme (Windows için).
*   **Dinamik Web Sayfası İşleme:** **Selenium** sayesinde JavaScript ile yüklenen veya dinamik olarak değişen sayfa içeriklerini başarıyla analiz etme.
*   **Kolay Kurulum ve Kullanım:** `webdriver_manager` ile Chrome sürücüsünün otomatik indirilmesi ve güncellenmesi.
*   **Yapılandırılabilir E-posta Ayarları:** SMTP sunucu bilgileri, gönderen ve alıcı adresleri script üzerinden kolayca ayarlanabilir.
*   **Güvenli Çıkış:** `KeyboardInterrupt` (Ctrl+C) ile programı güvenli bir şekilde sonlandırabilme ve tarayıcıyı kapatma.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

*   **Programlama Dili:** Python 3.x
*   **Web Otomasyonu:**
    *   `selenium`: Tarayıcı otomasyonu için temel kütüphane.
    *   `webdriver_manager`: Tarayıcı sürücülerinin (örn: ChromeDriver) otomatik yönetimi için.
*   **E-posta Gönderimi:**
    *   `smtplib`: SMTP protokolü üzerinden e-posta göndermek için Python'ın standart kütüphanesi.
    *   `email.mime.text` ve `email.mime.multipart`: E-posta mesajlarını oluşturmak ve biçimlendirmek için.
*   **Diğer Kütüphaneler:**
    *   `time`: Periyodik kontroller arasında bekleme süresi (`time.sleep()`) için.
    *   `winsound`: Windows sistemlerinde sesli uyarı (`Beep()`) için (Platforma özel).

---

## ⚙️ Kurulum ve Yapılandırma

Bu script'i çalıştırmadan önce aşağıdaki adımları takip etmeniz gerekmektedir:

1.  **Python 3 Kurulumu:**
    Eğer sisteminizde Python 3 yüklü değilse, [python.org](https://www.python.org/downloads/) adresinden indirip kurun. Kurulum sırasında "Add Python to PATH" seçeneğini işaretlemeyi unutmayın.

2.  **Gerekli Kütüphanelerin Kurulumu:**
    Terminal veya komut istemcisini açın ve aşağıdaki komutları çalıştırarak gerekli Python kütüphanelerini yükleyin:
    ```bash
    pip install selenium webdriver-manager
    ```
    *(Not: `winsound` kütüphanesi Windows'ta Python ile birlikte gelir, ek bir kurulum gerektirmez. Farklı bir işletim sistemi kullanıyorsanız, sesli uyarı için alternatif bir kütüphane/yöntem düşünülmelidir.)*

3.  **Google Chrome Tarayıcısı:**
    Script, Google Chrome tarayıcısı ile çalışacak şekilde ayarlanmıştır. Sisteminizde Google Chrome'un yüklü olduğundan emin olun.

4.  **E-posta Gönderen Ayarları:**
    Script içerisindeki aşağıdaki değişkenleri **kendi e-posta gönderici hesap bilgilerinizle** doldurmanız gerekmektedir:
    ```python
    MAILHOST = "smtp.example.com"  # E-posta sağlayıcınızın SMTP sunucu adresi (örn: "smtp.gmail.com")
    USERNAME = "your_email@example.com"  # Gönderici e-posta adresiniz
    PASSWORD = "your_email_password"  # Gönderici e-posta şifreniz (Dikkat! Güvenlik!)
    SEND_FROM = "your_email@example.com" # Gönderen olarak görünecek e-posta
    SEND_FROM_NAME = "Ürün Takip Botu" # Gönderen olarak görünecek isim
    REPLY_TO = "reply_to_email@example.com" # Yanıtlanacak e-posta (isteğe bağlı)
    REPLY_TO_NAME = "Destek" # Yanıtlanacak isim (isteğe bağlı)
    ```
    **Önemli Güvenlik Notu:** E-posta şifrenizi doğrudan koda yazmak güvenlik açısından risklidir. Daha güvenli yöntemler için ortam değişkenleri (environment variables) veya ayrı bir yapılandırma dosyası kullanmayı düşünebilirsiniz.
    *   **Gmail Kullanıcıları İçin:** Gmail ile SMTP üzerinden e-posta göndermek için "Daha az güvenli uygulama erişimi" ayarını açmanız veya "Uygulama Şifresi" oluşturmanız gerekebilir. Google, güvenlik nedeniyle bu tür erişimleri kısıtlamaktadır.

---

## 🚀 Nasıl Çalıştırılır?

1.  Yukarıdaki "Kurulum ve Yapılandırma" adımlarını tamamladığınızdan emin olun.
2.  Script dosyasını (`.py` uzantılı) bilgisayarınıza kaydedin.
3.  Bir terminal veya komut istemcisi açın.
4.  Script'in kaydedildiği dizine gidin (`cd path/to/your/script`).
5.  Script'i aşağıdaki komutla çalıştırın:
    ```bash
    python script_dosya_adi.py
    ```
6.  Program sizden sırasıyla aşağıdaki bilgileri girmenizi isteyecektir:
    *   Bildirim e-postalarının gönderileceği hedef e-posta adresi.
    *   Kaç adet ürün linki takip etmek istediğiniz.
    *   Takip etmek istediğiniz beden numarası.
    *   Takip edilecek ürünlerin linkleri (her birini ayrı ayrı girin).
7.  Bilgileri girdikten sonra script çalışmaya başlayacak ve periyodik olarak ürünleri kontrol edecektir. İstenen beden ve stok durumu bulunduğunda size bildirim gönderecektir.
8.  Script'i durdurmak için terminalde `Ctrl+C` tuş kombinasyonunu kullanabilirsiniz.

---

## 🧠 Nasıl Çalışıyor? (Teknik Detaylar)

1.  **WebDriver Başlatma:**
    *   `selenium.webdriver.ChromeOptions()` ile tarayıcı seçenekleri ayarlanır (örn: tam ekran başlama, eklentileri devre dışı bırakma).
    *   `webdriver_manager.chrome.ChromeDriverManager().install()` ile uyumlu ChromeDriver sürümü otomatik olarak indirilir ve ayarlanır.
    *   `webdriver.Chrome()` ile Chrome tarayıcı bir örneği başlatılır.

2.  **Kullanıcı Girdileri:**
    *   Program, kullanıcıdan hedef e-posta, takip edilecek link sayısı, istenen beden ve ürün linklerini alır.

3.  **Ana Kontrol Döngüsü:**
    *   Script, `while True` döngüsü içinde sürekli çalışır.
    *   Her bir döngüde, kullanıcı tarafından girilen tüm ürün linklerini tek tek ziyaret eder.

4.  **Sayfa Analizi ve Stok Kontrolü:**
    *   `driver.get(link)` ile belirtilen ürün sayfasına gidilir.
    *   Sayfa yüklendikten sonra, `driver.find_elements(By.CLASS_NAME, "size-selector-sizes-size__button")` komutu ile beden seçeneklerini içeren `<li>` elementleri bulunur. Bu class adı, takip edilen web sitesinin HTML yapısına özgüdür.
    *   Her bir beden (`<li>`) elementi için:
        *   İçerisindeki `size-selector-sizes-size__info` class'lı alt element incelenir.
        *   Bu alt elementin içinde `size-selector-sizes-size__availability` (stokta yok uyarısı) veya `size-selector-sizes-size__view-similars` (benzer ürünleri göster uyarısı) class'larına sahip elementlerin **bulunmadığı** kontrol edilir. Bu, bedenin stokta olabileceği anlamına gelir.
        *   Eğer beden stokta görünüyorsa, `size-selector-sizes-size__label` class'lı elementten beden etiketi (`M (US M)` gibi) okunur ve kullanıcının girdiği hedef beden ile karşılaştırılır.
    *   Eşleşme bulunursa (`found = True`):
        *   Konsola başarı mesajı yazdırılır.
        *   `winsound.Beep(1000, 1000)` ile sesli uyarı verilir.
        *   `send_email()` fonksiyonu çağrılarak kullanıcıya e-posta gönderilir.

5.  **E-posta Gönderme (`send_email` fonksiyonu):**
    *   `MIMEMultipart` ve `MIMEText` kullanarak e-posta mesajı oluşturulur (Gönderen, Alıcı, Konu, İçerik, Yanıt Adresi).
    *   `smtplib.SMTP()` ile yapılandırılan SMTP sunucusuna (örn: Gmail) 587 portu üzerinden bağlanılır.
    *   `server.starttls()` ile TLS şifrelemesi başlatılır.
    *   `server.login()` ile gönderici e-posta hesabına giriş yapılır.
    *   `server.sendmail()` ile e-posta gönderilir.
    *   `server.quit()` ile sunucu bağlantısı sonlandırılır.
    *   Hata durumunda `try-except` bloğu ile hata yakalanır ve konsola yazdırılır.

6.  **Bekleme ve Tekrar:**
    *   Tüm linkler kontrol edildikten sonra, script `time.sleep(30)` komutu ile 30 saniye bekler ve ardından döngüye baştan başlar.

7.  **Program Sonlandırma:**
    *   Kullanıcı `Ctrl+C` tuşlarına bastığında `KeyboardInterrupt` hatası yakalanır, "Uygulama sonlandırılıyor..." mesajı yazdırılır ve `finally` bloğunda `driver.quit()` komutu ile tarayıcı kapatılarak kaynaklar serbest bırakılır.

---

## ⚠️ Önemli Notlar ve Sınırlamalar

*   **Web Sitesi Bağımlılığı:** Bu script'in çalışması, hedef e-ticaret sitesinin HTML yapısına (class adları, element hiyerarşisi vb.) **doğrudan bağlıdır.** Eğer web sitesi tasarımını veya kod yapısını değiştirirse, script'in ürün ve beden bilgilerini bulmak için kullandığı seçiciler (`By.CLASS_NAME` değerleri) geçersiz kalabilir ve script hata verebilir veya yanlış çalışabilir. Bu durumda script'in güncellenmesi gerekir.
*   **Hız Sınırlamaları ve Engelleme Riski:** Çok sık ve otomatik istek gönderilmesi, bazı web siteleri tarafından bot aktivitesi olarak algılanabilir ve IP adresinizin geçici veya kalıcı olarak engellenmesine yol açabilir. Eğer sık sık hata alıyorsanız veya siteye erişiminiz engelleniyorsa, `time.sleep()` süresini artırmayı (örn: 60, 120 saniye veya daha fazla) düşünebilirsiniz.
*   **`winsound` Kütüphanesi:** `winsound.Beep()` fonksiyonu sadece Windows işletim sistemlerinde çalışır. Linux veya macOS gibi farklı sistemlerde sesli uyarı için alternatif kütüphaneler (örn: `playsound`, `simpleaudio`) veya sistem komutları kullanılmalıdır.
*   **Dinamik İçerik ve Yükleme Süreleri:** Selenium çoğu dinamik içeriği işleyebilse de, çok karmaşık JavaScript uygulamaları veya yavaş yüklenen sayfalar için ek `WebDriverWait` ve `expected_conditions` gibi Selenium bekleme mekanizmalarının entegre edilmesi gerekebilir.
*   **Hata Yönetimi:** Script temel hata yönetimi (`try-except`) içerir, ancak daha spesifik hatalar (örn: ağ bağlantısı sorunları, element bulunamama hatalarının daha detaylı işlenmesi) için geliştirilebilir.

---

## 🚀 Gelecekteki Geliştirmeler İçin Fikirler

*   **Grafiksel Kullanıcı Arayüzü (GUI):** `Tkinter`, `PyQt` veya `Kivy` gibi kütüphanelerle kullanıcı dostu bir arayüz eklenebilir.
*   **Yapılandırma Dosyası:** E-posta ayarları, linkler ve beden gibi bilgilerin script içinden değil, ayrı bir `.ini` veya `.json` yapılandırma dosyasından okunması.
*   **Farklı E-ticaret Siteleri İçin Destek:** Farklı sitelerin HTML yapılarına uyum sağlayabilecek daha esnek bir seçici mekanizması veya siteye özel konfigürasyonlar.
*   **Proxy Desteği:** IP engellemelerini aşmak için proxy sunucu kullanma seçeneği.
*   **Daha Gelişmiş Bildirimler:** Telegram botu, Discord webhook'u veya mobil anlık bildirim servisleri ile entegrasyon.
*   **Başsız (Headless) Mod:** Tarayıcı arayüzü görünmeden arka planda çalışma seçeneği (`options.add_argument("--headless")`).
*   **Asenkron Çalışma:** Birden fazla linki eş zamanlı kontrol etmek için `asyncio` kullanılabilir.

---

## 📜 Sorumluluk Reddi

Bu script, eğitim ve kişisel kullanım amaçlı olarak paylaşılmıştır. Lütfen bu aracı kullanırken:
*   **Etik kurallara uyun.**
*   Hedef web sitelerinin **Kullanım Şartları'na (Terms of Service)** saygı gösterin. Otomatik sorgulama ve veri çekme işlemleri bazı siteler tarafından yasaklanmış olabilir.
*   Script'i web sitelerine aşırı yük bindirecek veya hizmetlerini aksatacak şekilde **kötü niyetli kullanmayın.**
*   Bu script'in kullanımından doğabilecek herhangi bir sorumluluk tamamen kullanıcıya aittir.

---

Bu güçlü ve pratik otomasyon script'i ile aradığınız ürünleri bir daha kaçırmamanız dileğiyle! 🤖💨
