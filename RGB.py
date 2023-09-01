from machine import Pin
from time import sleep
import time
G= Pin(20,Pin.OUT)
B= Pin(21,Pin.OUT)
R= Pin(19,Pin.OUT)
ai=Pin(2, Pin.IN, Pin.PULL_UP)
ae=Pin(3, Pin.IN, Pin.PULL_UP)
ao=Pin(4, Pin.IN, Pin.PULL_UP)


while True:
    a =ai.value()
    b =ae.value()
    c =ao.value()
    if a == 0:
        G.value(255)
        B.value(0)
        R.value(0)
        print("G")
    elif b == 0:
        G.value(0)
        B.value(255)
        R.value(0)
        print("B")
    elif c == 0:
        G.value(0)
        B.value(0)
        R.value(255)
        print("R")
    else:
        G.value(0)
        B.value(0)
        R.value(0)
