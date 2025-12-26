import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = KMKKeyboard()
macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)

PINS = [board.D3, board.D4, board.D2, board.D1]
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

encoder_handler.pins = ((board.D5, board.D6, board.D7),)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]

i2c = busio.I2C(board.SCL, board.SDA)
oled_data = OledData(corner_one={0:OledReactionType.STATIC,1:["Layer"]})
oled_ext = Oled(oled_data, toDisplay=OledDisplayMode.TXT, flip=False)
keyboard.extensions.append(oled_ext)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D],
]

if __name__ == '__main__':
    keyboard.go()
