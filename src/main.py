from OLED128x64 import OLED128x64
import utime
import network


def setup():
    oled = OLED128x64(sda_pin=4, scl_pin=5)
    oled.clear()
    oled.display_text("Power Connected!", x=0, y=0)
    utime.sleep(1)
    oled.clear()


def wifi():
    # Fill in your WiFi network name (ssid) and password here:
    wifi_ssid = "voronet-TEMP"
    wifi_password = "C1derD0nut"

    # Connect to WiFi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(wifi_ssid, wifi_password)
    
    oled = OLED128x64(sda_pin=4, scl_pin=5)
    oled.display_text("Wait for WiFi...", x=0, y=0)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        utime.sleep(1)
    
    oled.clear()
    oled.display_text("WiFi Connected!", x=0, y=0)
    # print ip
    ip = wlan.ifconfig()[0]
    oled.display_text(ip, x=0, y=16)
    utime.sleep(3)
    oled.clear()
    
    print("Connected to WiFi")



if __name__ == "__main__":
    setup()
    wifi()
    while True:
        pass