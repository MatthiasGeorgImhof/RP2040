import neopixel
import time

GPIO_OUT = (3,5,27,29)
GPIO_IN = 14

is_running = False
switch_is_active = False
switch_was_active = switch_is_active

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
delays =  (0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.90, 0.10)

switch = machine.Pin(GPIO_IN, machine.Pin.IN, machine.Pin.PULL_DOWN)

hw_pins = tuple(machine.Pin(n, machine.Pin.OUT) for n in GPIO_OUT)
neo_pixels = tuple(neopixel.NeoPixel(hw_pins[n],4) for n in range(len(dddd)))

def set_rgb(neo_pixel, color):
    for i,rgb in enumerate(color):
        neo_pixel[i] = rgb
        neo_pixel.write()

def set_all_dark():
          for neo_pixel in neo_pixels:
              set_rgb(neo_pixel, dddd)

set_all_dark()

while(True):
  for delay, color0, color1, color2, color3 in zip(delays, colors0, colors1, colors2, colors3):
      switch_is_active = switch.value()
      if switch_is_active and not switch_was_active:
          is_running = not is_running
      
      if is_running:
          colors = (color0, color1, color2, color3)
          for neo_pixel, color in zip(neo_pixels, colors):
              set_rgb(neo_pixel, color)
      else:
          set_all_dark()
    
      time.sleep(delay)
      switch_was_active = switch_is_active