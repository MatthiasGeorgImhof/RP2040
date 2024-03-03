import neopixel
import time
p = machine.Pin.board.GP3
n = neopixel.NeoPixel(p,4)

#is rgb

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
orange = (255,40,0)
dark = (0,0,0)

signals = (
    (0.1, (white, white, red, red)),
    (0.1, (dark, white, red, dark)),
    (0.1, (white, white, red, red)),
    (0.1, (dark, white, red, dark)),
    (0.1, (white, white, red, red)),
    (0.1, (dark, white, red, dark)),
    (0.9, (white, white, red, red)),
    )
  
while(True):
  for delay, colors in signals:
      for i,rgb in enumerate(colors):
         n[i] = rgb
      n.write()
      time.sleep(delay)