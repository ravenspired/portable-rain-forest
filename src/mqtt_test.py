import time
from wifi import WiFi
from mqtt import MQTT

SSID = "voronet-TEMP"
PASSWORD = "C1derD0nut"
BROKER = "192.168.1.21"
TOPIC = "test/topic"

def message_callback(msg):
    print("Received message:", msg)

wifi = WiFi(SSID, PASSWORD)
mqtt = MQTT("pico_client", BROKER)
mqtt.subscribe(TOPIC, message_callback)

i = 0
while True:
    wifi.check_connection()
    msg = f"Hello from Pico W! Count: {i}"
    mqtt.publish(TOPIC, msg)
    print("Published:", msg)
    i += 1
    mqtt.check_messages()
    time.sleep(5)
