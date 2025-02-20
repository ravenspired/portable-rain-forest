import time
from wifi import WiFi
from CapacitiveSoilMoistureSensor import SoilMoistureSensor
from mqtt import MQTT

# WiFi configuration
WIFI_SSID = 'voronet-TEMP'
WIFI_PASSWORD = 'C1derD0nut'

# MQTT configuration
MQTT_BROKER = '192.168.1.21'
MQTT_PORT = 1883
MQTT_TOPIC = 'plants/pitcher/data'

# Initialize WiFi
wifi = WiFi(WIFI_SSID, WIFI_PASSWORD)


# Initialize MQTT client
mqtt_client = MQTT('soil_moisture_client', MQTT_BROKER)

# Initialize soil moisture sensor
soil_sensor = SoilMoistureSensor(28)

def publish_soil_moisture():
    while True:
        # Read soil moisture data
        soil_moisture = soil_sensor.read_average_moisture()
        
        # Publish data to MQTT topic
        mqtt_client.publish(MQTT_TOPIC, str(soil_moisture))
        print(f"Soil Moisture Level: {soil_moisture}")
        
        # Wait for 1 second
        time.sleep(1)

if __name__ == '__main__':
    publish_soil_moisture()
