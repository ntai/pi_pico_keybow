#

from adafruit_hid.keycode import Keycode

SHORTCUTS = [
  "uesrname",
  "password",
  None,
  None,
  [(Keycode.T, Keycode.COMMAND, Keycode.OPTION), (Keycode.N, Keycode.COMMAND), "cmd1\n"],
  [(Keycode.T, Keycode.COMMAND, Keycode.OPTION), (Keycode.N, Keycode.COMMAND), "cmd2\n"],
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  None,
  ":lol:",
  ]
