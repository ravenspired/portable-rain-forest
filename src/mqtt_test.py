# Anton Voronov, ravenspired, voronet.net
# This script connects a Raspberry Pi Pico to a WiFi network and an MQTT broker to publish messages periodically.
# Classes:
#     None
# Functions:
#     message_callback(msg): Callback function that prints received MQTT messages.
# Constants:
#     SSID (str): WiFi network name.
#     PASSWORD (str): WiFi network password.
#     BROKER (str): MQTT broker IP address.
#     TOPIC (str): MQTT topic to publish and subscribe to.
# Usage:
#     The script initializes a WiFi connection and an MQTT client. It subscribes to a specified topic and publishes a message every 5 seconds. The message includes a count that increments with each publication. Received messages are printed to the console.


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