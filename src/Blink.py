# Anton Voronov, ravenspired, voronet.net
# Blink LED Class

# This class is used to control an LED connected to a digital pin on the Raspberry Pi Pico.
# The LED is connected to a digital pin on the Pico, and the Pico can turn the LED on and off by setting the pin high or low.
# The BlinkLED class provides a simple interface to control the LED by toggling it on and off at specified intervals.
# The class has an update method that can be called periodically to update the LED state based on the specified on and off times.

# The LED is connected to pin "LED" on the Pico W, which is the built-in LED on the board.


from machine import Pin
import utime

class BlinkLED:
    def __init__(self, pin_number, on_time=100, off_time=100):
        self.led = Pin(pin_number, Pin.OUT)
        self.on_time = on_time
        self.off_time = off_time
        self.last_toggle_time = utime.ticks_ms()
        self.state = False

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
    should_blink = True

    led_blinker = BlinkLED("LED", on_time=50, off_time=50)

    while True:
        if should_blink:
            led_blinker.update(on_time=200, off_time=200)  # Adjust the speed here
            utime.sleep(0.01)
        else:
            led_blinker.led.off()
            utime.sleep(0.01)
