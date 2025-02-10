import network
import time
import machine
from umqtt.simple import MQTTClient

# WiFi Credentials
SSID = "voronet-TEMP"
PASSWORD = "C1derD0nut"

# MQTT Broker Settings
MQTT_BROKER = "mqtt_broker_address"
MQTT_TOPIC = "home/water_level"

# GPIO Setup
SENSOR_PIN = 15  # Change based on your wiring
sensor = machine.Pin(SENSOR_PIN, machine.Pin.IN)

# Connect to WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)

    print("Connected to WiFi:", wlan.ifconfig())

# Connect to MQTT Broker
def connect_mqtt():
    client = MQTTClient("pico_w", MQTT_BROKER)
    client.connect()
    print("Connected to MQTT Broker:", MQTT_BROKER)
    return client

# Main loop
def main():
    connect_wifi()
    client = connect_mqtt()

    while True:
        water_level = "LOW" if sensor.value() == 0 else "HIGH"
        print(f"Water Level: {water_level}")
        client.publish(MQTT_TOPIC, water_level.encode())

        time.sleep(5)  # Adjust the frequency of updates

try:
    main()
except Exception as e:
    print("Error:", e)
    machine.reset()  # Restart on failure
