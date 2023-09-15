import machine
import onewire
import ds18x20
import time

# Set the GPIO pin for DS18B20 data
ds18b20_pin = machine.Pin(4)  # Replace with the actual GPIO pin number you used for the data pin.

# Create a DS18X20 sensor object
ds = ds18x20.DS18X20(onewire.OneWire(ds18b20_pin))

# Scan for DS18B20 devices on the bus
roms = ds.scan()

if not roms:
    raise Exception("No DS18B20 devices found")

try:
    while True:
        # Trigger a temperature conversion for all DS18B20 sensors
        ds.convert_temp()

        # Wait for the conversion to finish (750ms for DS18B20)
        time.sleep_ms(750)

        # Read and print temperature values for all DS18B20 sensors
        for rom in roms:
            temperature = ds.read_temp(rom)
            print(f"Sensor {rom.hex()} - Temperature: {temperature:.2f}°C")

        # Wait for a few seconds before the next reading
        time.sleep(5)

except KeyboardInterrupt:
    print('Program terminated by user')