from machine import ADC, Pin
import utime

from WaterSensor import WaterSensor
from Blink import BlinkLED


class BlinkingLED:
    def __init__(self, pin_number, on_time=100, off_time=100):
        self.led = Pin(pin_number, Pin.OUT)
        self.on_time = on_time
        self.off_time = off_time
        self.last_toggle_time = utime.ticks_ms()
        self.state = False
        self.led.off()

    def update(self, on_time=None, off_time=None):
        # Use the provided on_time and off_time, or default to the object's values
        if on_time is not None:
            self.on_time = on_time
        if off_time is not None:
            self.off_time = off_time

        current_time = utime.ticks_ms()
        if self.state and utime.ticks_diff(current_time, self.last_toggle_time) >= self.on_time:
            self.led.off()
            self.state = False
            self.last_toggle_time = current_time
        elif not self.state and utime.ticks_diff(current_time, self.last_toggle_time) >= self.off_time:
            self.led.on()
            self.state = True
            self.last_toggle_time = current_time


if __name__ == "__main__":
    water_sensor = WaterLevelSensor(26, threshold1=30000, threshold2=50000, threshold3=60000)
    led_blinker = BlinkingLED("LED")
    last_check_time = utime.ticks_ms()
    water_level_check_interval = 1 * 1000  # 5 seconds
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
