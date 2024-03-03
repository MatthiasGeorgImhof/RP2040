import neopixel
import time

switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
is_running = True

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
orange = (200,80,0)
dark = (0,0,0)

wwgg = (white, white, green, green)
wwrr = (white, white, red, red)
oorr = (orange, orange, green, green)
oogg = (orange, orange, red, red)
dddd = (dark, dark, dark, dark)

colors0 = (wwgg, dddd, wwgg, dddd, wwgg, dddd, wwgg, dddd)
colors1 = (wwrr, dddd, wwrr, dddd, wwrr, dddd, wwrr, dddd)
colors2 = (oogg, dddd, oogg, dddd, oogg, dddd, oogg, dddd)
colors3 = (oorr, dddd, oorr, dddd, oorr, dddd, oorr, dddd)
delays =  (0.01,  0.19, 0.01, 0.19, 0.01, 0.19,  0.9,  0.1)

pin_numbers = (3,5,27,29)
hw_pins = tuple(machine.Pin(n, machine.Pin.OUT) for n in pin_numbers)
neo_pixels = tuple(neopixel.NeoPixel(hw_pins[n],4) for n in range(4))

#is rgb

def set_all_dark():
          for neo_pixel in neo_pixels:
              for i,rgb in enumerate(dddd):
                  neo_pixel[i] = rgb
                  neo_pixel.write()

set_all_dark()
is_running = False

while(True):
  for delay, color0, color1, color2, color3 in zip(delays, colors0, colors1, colors2, colors3):
      if switch.value():
          print("switch", is_running)
          is_running = not is_running
      if is_running:
          colors = (color0, color1, color2, color3)
          for neo_pixel, color in zip(neo_pixels, colors):
              for i,rgb in enumerate(color):
                  neo_pixel[i] = rgb
                  neo_pixel.write()
      else:
          set_all_dark()
      time.sleep(delay)