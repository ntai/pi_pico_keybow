# pi_pico_keybow
Keybow with Raspberry Pi Pico

## Ingredients
1. CircuitPython - https://circuitpython.org/board/raspberry_pi_pico/  As of 2022-05-30, version 7.3.0.
2. libraries - the `lib` directory in the repo is the library I used.
3. code.py and shortcuts.py

## code.py
Decided to split out the key assignments (aka shortcuts) from code.py.
As I now have 2 keybows (Yes, I liked it a lot), it's more sanitary to have the data part (shortcuts.py) separate from the code.

## shortcuts.py
The shortcut entry is either a string literal or a list of keycode + string. There should be 16 entries.


