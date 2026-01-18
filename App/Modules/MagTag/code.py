# This code.py file contains Coworking space manager code for the MagTag

import time
from adafruit_magtag.magtag import MagTag

import board
import neopixel


magtag = MagTag()

magtag.add_text(
    text_position=(
        10,
        (magtag.graphics.display.height // 2) - 1,
    ),
    text_scale=3,
)

magtag.set_text("Conference room")

button_colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255))
button_tones = (1047, 1318, 1568, 2093)



# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.D10


# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

global_state = 0
global_brightness = (0, 0, 0)


def update_brightness():
    """update_brightness is code to adjust colour and brightness depending
    on the global state"""
    state = global_state

    state = global_state + 1

    if state > 2:
        state = 0

    if state == 0:
        colours = (0, 0, 0) # LEDs off
        magtag.set_text("Conference room")
    elif state == 1:
        colours = (0, 85*3, 0) # LEDs green max
        magtag.set_text("Room is now Free")
    elif state == 2:
        colours = (85*3, 0, 0) # LEDs red
        magtag.set_text("Room is Booked")

    return colours, state

# Loop forever
while True:

    if magtag.peripherals.button_a_pressed:
        global_brightness, global_state = update_brightness()

        pixels.fill(global_brightness)
        pixels.show()

        # Wait a little bit
        time.sleep(0.2)
    else:
        pass