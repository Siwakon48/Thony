import max7219
import machine
import onewire
import ds18x20
import time
from machine import Pin, SPI
from time import sleep

# DS18B20 setup
ds18b20_pin = machine.Pin(4)
ds = ds18x20.DS18X20(onewire.OneWire(ds18b20_pin))
roms = ds.scan()

# MAX7219 LED matrix display setup
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 4)
display.brightness(1)  # adjust brightness 1 to 15

if not roms:
    raise Exception("No DS18B20 devices found")

try:
    while True:
        ds.convert_temp()
        time.sleep_ms(750)

        for rom in roms:
            temperature = ds.read_temp(rom)
            temperature_str = f"{temperature:.2f}C"
            print(f"Sensor {rom.hex()} - Temperature: {temperature_str}")
            
            # Display the temperature on the MAX7219 display
            display.fill(0)
            display.text(temperature_str, 0, 0, 1)
            display.show()

        time.sleep(4)

except KeyboardInterrupt:
    print('terminated')