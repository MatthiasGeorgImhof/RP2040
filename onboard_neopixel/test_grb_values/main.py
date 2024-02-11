import neopixel
import time
p = machine.Pin.board.GP16
n = neopixel.NeoPixel(p,1)

green = (255,0,0)
red = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
orange = (40,255,0)

n[0] = orange
n.write()