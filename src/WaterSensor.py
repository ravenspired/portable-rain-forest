# Anton Voronov, ravenspired, voronet.net
# Water Level Sensor Class

# This class is used to read the water level from a water sensor connected to an analog pin on the Raspberry Pi Pico.
# The water sensor is a resistive sensor that changes resistance based on the water level.
# The sensor is connected to an analog pin on the Pico, and the Pico reads the analog voltage from the sensor.
# The Pico then converts the analog voltage to a digital value using the ADC (Analog to Digital Converter) module.
# The digital value is then used to determine the water level based on predefined thresholds.
# The thresholds are set based on the sensor's resistance values at different water levels.
# The water level is classified as low, medium, or high based on the thresholds.



# The sensor has three wires: VCC, GND, and OUT.
# Connect the VCC wire to 3V3, the GND wire to GND, and the OUT wire to the analog pin (26) on the Pico.

from machine import ADC, Pin
import utime


class WaterSensor:
    def __init__(self, pin_number, threshold1, threshold2, threshold3):
        self.sensor = ADC(Pin(pin_number))
        self.thresholds = [threshold1, threshold2, threshold3]

    def read_average_level(self, samples=20):
        total = 0
        for _ in range(samples):
            total += self.sensor.read_u16()
            utime.sleep_ms(10)
        return total / samples

    def get_water_level(self, samples=20):
        level = self.read_average_level(samples)
        if level < self.thresholds[0]:
            return "low"
        elif level < self.thresholds[1]:
            return "medium"
        else:
            return "high"

if __name__ == "__main__":
    water_sensor = WaterSensor(26, threshold1=30000, threshold2=50000, threshold3=60000)
    last_check_time = utime.ticks_ms()
    check_interval = 1000  # 5 seconds

    while True:
        current_time = utime.ticks_ms()
        
        # Check water level every 5 seconds
        if utime.ticks_diff(current_time, last_check_time) >= check_interval:
            water_level = water_sensor.get_water_level()
            last_check_time = current_time
            print(f"Water Level: {water_level}")
        
        utime.sleep_ms(10)
