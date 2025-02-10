from machine import Pin
import time
from dht import DHT11
 
sensor = DHT11(Pin(16, Pin.OUT, Pin.PULL_DOWN))
 
while True:
    temp = int(sensor.temperature())
    humidity = int(sensor.humidity())
    print("Temperature: {}C   Humidity: {:.0f}% ".format(temp, humidity))
    time.sleep(2)