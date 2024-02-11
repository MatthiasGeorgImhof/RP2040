import neopixel
import time
p = machine.Pin.board.GP16
n = neopixel.NeoPixel(p,1)
while(True):
    for g in range(0,255,16):
        for r in range(0,255,16):
            for b in range(0,255,16):
                n[0] = (g,r,b)
                n.write()
                time.sleep(0.05)