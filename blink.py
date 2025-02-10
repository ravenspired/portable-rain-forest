from machine import Pin
from utime import sleep

pin = Pin("LED", machine.Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1)  # sleep 1 second
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")