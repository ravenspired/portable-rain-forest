# Anton Voronov, ravenspired, voronet.net
# WiFi Class



import network
import time

class WiFi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.connected = False
        self.connect()

    def connect(self):
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        print("Connecting to WiFi...")
        
        for _ in range(10):  # Retry for 10 seconds
            if self.wlan.isconnected():
                self.connected = True
                print("Connected! IP:", self.wlan.ifconfig()[0])
                return
            time.sleep(1)
        
        print("Failed to connect to WiFi.")
        self.connected = False

    def check_connection(self):
        if not self.wlan.isconnected():
            print("WiFi lost. Reconnecting...")
            self.connect()