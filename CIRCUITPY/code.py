#

import math
from keybow2040 import Keybow2040, number_to_xy, hsv_to_rgb
# from keybow_hardware.pim56x import PIM56X as Hardware # for Keybow 2040
from keybow_hardware.pim551 import PIM551 as Hardware # for Pico RGB Keypad Base

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Set up Keybow
keybow = Keybow2040(Hardware())

keys = [None] * 16
for index in range(16):
    rearranged = 3 - (math.floor(index / 4)) + ((index % 4) * 4)
    keys[index] = keybow.keys[rearranged]

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

from shortcuts import SHORTCUTS

MAP = {}

for index in range(16):
    MAP[keys[index]] = SHORTCUTS[index]

    def press_handler(key):
        if isinstance(MAP[key], str):
            layout.write(MAP[key])
        else:
            for kc in MAP[key]:
                if isinstance(kc, str):
                    layout.write(kc)
                else:
                    keyboard.send(*kc)
                    pass
                pass
            pass
        pass

    if SHORTCUTS[index]:
        keybow.on_press(keys[index], handler=press_handler)


def rainbow(step):
    for i in range(16):
        # Convert the key number to an x/y coordinate to calculate the hue
        # in a matrix style-y.
        x, y = number_to_xy(i)

        # Calculate the hue.
        hue = (x + y + (step / 20)) / 8
        hue = hue - int(hue)
        hue = hue - math.floor(hue)

        # Convert the hue to RGB values.
        r, g, b = hsv_to_rgb(hue, 1, 1)

        # Display it on the key!
        keys[i].set_led(r, g, b)


#
for index in range(0, 64):
    rainbow(index)

#
pressed_color = (0, 255, 255)
black = (0, 0, 0)

def reactive():
    # Loop through the keys and set the LED to cyan if pressed, otherwise turn
    # it off (set it to black).
    for key in keys:
        if key.pressed:
            key.set_led(*pressed_color)
        else:
            key.set_led(*black)

# Increment step to shift animation across keys.
step = 0

while True:
    # Always remember to call keybow.update() on every iteration of your loop!
    keybow.update()

    step += 1
    # rainbow(step)
    reactive()
