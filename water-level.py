# Anton Voronov, ravenspired, voronet.net
# Water Level Monitoring System

# This script combines the WaterSensor and BlinkLED classes to create a water level monitoring system.
# The system reads the water level from a water sensor connected to an analog pin on the Raspberry Pi Pico.
# The water level is classified as low, medium, or high based on predefined thresholds.
# The system controls an LED connected to a digital pin on the Pico to indicate the water level.
# The LED blinks at different rates based on the water level: slow blink for medium, fast blink for low, and off for high.
# The system checks the water level every 5 seconds and updates the LED accordingly.

# The water sensor has three wires: VCC, GND, and OUT. Connect the VCC wire to 3V3, the GND wire to GND, and the OUT wire to the analog pin (26) on the Pico.
# The LED is connected to pin "LED" on the Pico W, which is the built-in LED on the board.  

from machine import ADC, Pin
import utime

from WaterSensor import WaterSensor
from Blink import BlinkLED


if __name__ == "__main__":
    water_sensor = WaterSensor(26, threshold1=30000, threshold2=50000, threshold3=60000)
    led_blinker = BlinkLED("LED")
    last_check_time = utime.ticks_ms()
    water_level_check_interval = 5 * 1000  # 5 seconds
    water_present = False

    while True:
        current_time = utime.ticks_ms()
        
        # Check water level every 5 seconds
        if utime.ticks_diff(current_time, last_check_time) >= water_level_check_interval:
            water_present = water_sensor.get_water_level()
            last_check_time = current_time
            print(f"Water Present: {water_present}")
        
        # Control LED blinking
        if water_present == "high":
            led_blinker.led.off()
        elif water_present == "medium":
            led_blinker.update(on_time=500, off_time=500)  # Slow blink
        elif water_present == "low":
            led_blinker.update(on_time=100, off_time=100)  # Fast blink
        
        utime.sleep_ms(10)
