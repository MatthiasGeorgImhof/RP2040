import neopixel
import time
p = machine.Pin.board.GP12
n = neopixel.NeoPixel(p,4)

#is rgb

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
orange = (255,40,0)
dark = (0,0,0)

n[0] = orange
n[1] = red
n[2] = grenn
n[3] = blue

n.write()