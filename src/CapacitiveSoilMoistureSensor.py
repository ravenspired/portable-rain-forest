# Anton Voronov, ravenspired, voronet.net
# Capacitive Soil Moisture Sensor Class
# 
# This class is used to read the soil moisture level from a capacitive soil moisture sensor connected to an analog pin on the Raspberry Pi Pico.
# The sensor provides an analog voltage that changes based on the moisture content in the soil.
# The Pico reads the analog voltage from the sensor and converts it to a digital value using the ADC (Analog to Digital Converter) module.
# The digital value is returned as a raw number without predefined thresholds.
#
# The sensor has three wires: VCC, GND, and OUT.
# Connect the VCC wire to 3V3, the GND wire to GND, and the OUT wire to the analog pin (28) on the Pico.

from machine import ADC, Pin
import utime

class SoilMoistureSensor:
    def __init__(self, pin_number):
        self.sensor = ADC(Pin(pin_number))

    def read_average_moisture(self, samples=10):
        total = 0
        for _ in range(samples):
            total += self.sensor.read_u16()
            utime.sleep_ms(10)
        return total / samples

if __name__ == "__main__":
    soil_sensor = SoilMoistureSensor(28)
    last_check_time = utime.ticks_ms()
    check_interval = 1000  # 1 second

    while True:
        current_time = utime.ticks_ms()
        
        # Check soil moisture level every second
        if utime.ticks_diff(current_time, last_check_time) >= check_interval:
            moisture_level = soil_sensor.read_average_moisture()
            last_check_time = current_time
            print(f"Soil Moisture Level: {moisture_level}")
        
        utime.sleep_ms(10)
