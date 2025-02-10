import machine
import ssd1306

class OLED128x64:
    def __init__(self, sda_pin, scl_pin, width=128, height=64, i2c_addr=0x3C):
        # Initialize the I2C interface
        self.i2c = machine.I2C(0, sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin))
        self.width = width
        self.height = height
        self.oled = ssd1306.SSD1306_I2C(self.width, self.height, self.i2c, addr=i2c_addr)
    
    def clear(self):
        """Clear the display."""
        self.oled.fill(0)
        self.oled.show()

    def display_text(self, text, x=0, y=0):
        """Display text on the OLED."""
        self.oled.text(text, x, y)
        self.oled.show()

    def draw_line(self, x1, y1, x2, y2):
        """Draw a line on the OLED."""
        self.oled.line(x1, y1, x2, y2, 1)
        self.oled.show()

    def draw_rectangle(self, x, y, w, h):
        """Draw a rectangle on the OLED."""
        self.oled.rect(x, y, w, h, 1)
        self.oled.show()

    def fill_rectangle(self, x, y, w, h):
        """Fill a rectangle on the OLED."""
        self.oled.fill_rect(x, y, w, h, 1)
        self.oled.show()

    def display_image(self, image_data):
        """Display an image from a byte array."""
        self.oled.blit(image_data, 0, 0)
        self.oled.show()

    def invert_display(self, invert=True):
        """Invert the display colors."""
        self.oled.invert(invert)

# Example usage
if __name__ == "__main__":
    # Initialize the OLED with SDA pin 4, SCL pin 5
    oled = OLED128x64(sda_pin=4, scl_pin=5)

    # Clear the display
    oled.clear()

    # Display text
    oled.display_text("Hello, World!", x=0, y=0)

    # Draw a line
    oled.draw_line(10, 10, 100, 50)

    # Draw a rectangle
    oled.draw_rectangle(20, 20, 40, 30)

    # Fill a rectangle
    oled.fill_rectangle(50, 50, 60, 20)
