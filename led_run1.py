from machine import Pin
from time import sleep


def ledrun():
    LEDS = [Pin(18,Pin.OUT),Pin(19,Pin.OUT),Pin(20,Pin.OUT)]
    
    while True:
        
        for  LED in LEDS:
             LED.on()
             sleep(0.5)
             
             LED.off()
             sleep(0.5)
             
ledrun()