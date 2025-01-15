import os
import subprocess
import sys
import requests

def check_adb_installed():
    """Check if ADB is installed and available in the PATH."""
    try:
        subprocess.run(["adb", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("ADB zaten yüklü.")
    except FileNotFoundError:
        print("ADB bulunamadı. Kurulum başlatılıyor...")
        install_adb()

def install_adb():
    """Install ADB if not already installed."""
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "adb"], check=True)
        print("ADB başarıyla kuruldu.")
    except subprocess.CalledProcessError:
        print("ADB kurulumu başarısız oldu.")
        sys.exit(1)

def check_device_connected():
    """Check if a device is connected via ADB."""
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    if result.returncode != 0:
        print("ADB cihaz bağlantısı sağlanamadı!")
        sys.exit(1)

    devices_output = result.stdout.strip()
    if "device" not in devices_output:
        print("Hiçbir cihaz bağlı değil. Lütfen cihazınızı bağlayın ve ADB modunu etkinleştirin.")
        sys.exit(1)
    else:
        print(f"Cihaz bağlantısı başarılı: {devices_output}")

def get_installed_packages():
    """Get the list of installed packages (APK names)."""
    result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
    if result.returncode != 0:
        print("APK listesi alınamadı.")
        sys.exit(1)

    # Extract package names from the output
    installed_packages = result.stdout.strip().splitlines()
    installed_packages = [pkg.split(":")[1] for pkg in installed_packages]
    return installed_packages

def load_vulnerable_packages():
    """Load vulnerable package names from the provided URL."""
    url = "https://gist.githubusercontent.com/fs0c131y/f498b21cba9ee23956fc7d7629262e9d/raw/5cbe04da03796ee3a2671f0b89a5b355eee6e18a/gistfile1.txt"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Vulnerable packages list alınamadı.")
        sys.exit(1)
    
    # Parse the response text into a set of vulnerable package names
    vulnerable_packages = set(response.text.strip().splitlines())
    return vulnerable_packages

def check_vulnerabilities(installed_packages, vulnerable_packages):
    """Check if any installed package matches known vulnerable packages."""
    print("\nZafiyetli APK'lar:")
    for pkg in installed_packages:
        if pkg in vulnerable_packages:
            print(f"Zafiyetli APK tespit edildi: {pkg}")
        

def main():
    """Main function to run the script."""
    check_adb_installed()
    check_device_connected()
    
    print("Cihazdan APK listesi alınıyor...")
    installed_packages = get_installed_packages()
    
    vulnerable_packages = load_vulnerable_packages()
    
    check_vulnerabilities(installed_packages, vulnerable_packages)
    print(f"Mobil cihazlardaki uygulamalara verilen izinlerin gözden geçirilmesi, gereksiz konum erişimlerinin kapatılması, Bu uygulamaların erişim izinlerini kısıtlamayı unutmayın!")
if __name__ == "__main__":
    main()
