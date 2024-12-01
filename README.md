Selenium ile Ürün Stok Takip Botu
Bu proje, Zara'nın internet sitesindeki ürünlerin belirli bedenlerinin stok durumunu kontrol etmek için geliştirilmiş bir Selenium botudur. Kullanıcıdan alınan ürün bağlantılarına ve hedef bedene göre düzenli olarak stok kontrolü yapılır. Kriterlere uygun bir ürün bulunduğunda sesli uyarı verir. Klavye'den CTRL + C Girişi bekler ve girdiyi almadan kapanmaz.
Programın tek amacı eğitimdir.

Özellikler
-Birden Fazla Ürünü Kontrol Etme: Kullanıcı birden fazla ürün linki ekleyebilir.
-Beden Seçimi: Hedef beden kullanıcıdan alınır ve sadece bu beden kontrol edilir.
-Periyodik Kontrol: Belirli bir zaman aralığıyla (30 saniye) ürünler tekrar kontrol edilir.
-Sesli Uyarı: Kriterlere uygun bir ürün bulunduğunda sesli bir uyarı çalar.
-Hata Yönetimi: Kontrol sırasında oluşabilecek hatalar konsola yazdırılı

Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki yazılımlar ve kütüphaneler gereklidir:

-Python 3.7 veya üstü
-Google Chrome (Güncel bir sürüm)
-ChromeDriver
-Aşağıdaki Python kütüphaneleri:
-selenium
-webdriver-manager
Bu kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:
-pip install selenium webdriver-manager

Kullanım

Projeyi Klonlayın veya İndirin
git clone https://github.com/nullablege/zara-stok-takip.git
cd urun-stok-takip-botu

Kodun Çalıştırılması
Python dosyasını çalıştırın:
python zara-stok-takip.py

ullanıcıdan Girdi Alın

Ürün Sayısı: Kontrol etmek istediğiniz ürün sayısını girin.
Beden: Takip etmek istediğiniz beden bilgisini girin (örneğin, L).

Ürün Linklerini Girin
Her ürün için bir URL girin. Örneğin:
( İlgili ürünün sitedeki sayfası ) 

Sonuçları İzleyin

Kriterlere uygun bir ürün bulunduğunda sesli uyarı alırsınız.
Bulunamadığında konsolda "Kriterlere uyan bir ürün bulunamadı." mesajını görürsünüz.
Kontrol işlemi her 30 saniyede bir tekrar eder.

Çıkış
Botu durdurmak için CTRL+C kombinasyonunu kullanın.
