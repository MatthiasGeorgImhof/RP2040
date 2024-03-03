import machine
import time

pin6 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
pin7 = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
pin8 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
pin9 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
pin14 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
pin15 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
pin26 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

while(True):
    #print(p.value())
    values = (pin6.value(), pin7.value(), pin8.value(), pin9.value(), pin13.value(), pin14.value(), pin15.value(), pin26.value())
    print(values)
    time.sleep(0.1)
    