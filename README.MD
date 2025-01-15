# Gravy Analytics APK Vulnerability Checker (2025)

Bu Python betiği, **Gravy Analytics** platformu için Android cihazlarda yüklü APK'ları kontrol eder ve bu uygulamaların güvenlik açıklarını tespit eder. Uygulama, cihazla bağlantı kurarak yüklü paketlerin listesini alır ve ardından bir liste ile karşılaştırarak güvenlik açığı taşıyan APK'ları ekrana yazdırır. Bu araç, Gravy Analytics tarafından geliştirilen uygulama güvenliği analizlerinin bir parçası olarak kullanılabilir.

## Özellikler

- **ADB Kontrolü**: Betik, Android Debug Bridge (ADB) aracının sisteminizde yüklü olup olmadığını kontrol eder. Eğer ADB yüklü değilse, otomatik olarak yükler.
- **Cihaz Bağlantısı Kontrolü**: Bağlı bir Android cihazın olup olmadığını kontrol eder. Cihaz bağlı değilse kullanıcıyı bilgilendirir.
- **Yüklü APK'ların Listesi**: Android cihazındaki tüm yüklü APK'ları listeler.
- **Zafiyetli APK Kontrolü**: Çevrimiçi bir kaynaktan alınan güvenlik açığına sahip APK'lar ile karşılaştırarak, cihazınızdaki zafiyetli uygulamaları tespit eder.

## Gereksinimler

### 1. ADB (Android Debug Bridge)
ADB, cihazınızla etkileşim kurmak için gereklidir. ADB'nin sisteminizde kurulu olup olmadığını kontrol eder, eğer kurulu değilse betik otomatik olarak yükler.

**Manuel Kurulum**:

- Ubuntu / Debian:
    ```bash
    sudo apt install adb
    ```

### 2. Python Kütüphaneleri
Betiğin çalışabilmesi için aşağıdaki Python kütüphanesine ihtiyaç vardır:
- `requests`: Güvenlik açığı taşıyan APK'ların listesini çevrimiçi kaynaktan almak için kullanılır.

Yukarıdaki kütüphaneyi yüklemek için terminale şu komutu girin:
```bash
pip install requests
