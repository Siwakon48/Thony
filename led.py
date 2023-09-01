from machine import Pin, Timer
led = Pin(25, Pin.OUT)
ledG = Pin(18, Pin.OUT)
ledY = Pin(19, Pin.OUT)
ledR = Pin(20, Pin.OUT)
timer = Timer()


def blink(timer):
    led.toggle()
    ledG.toggle()
    ledY.toggle()
    ledR.toggle()
    

timer.init(freq=5, mode=Timer.PERIODIC, callback=blink)