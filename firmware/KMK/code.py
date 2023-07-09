# Adafruit CircuitPython 8.0.5 on 2023-03-31; Waveshare RP2040-Zero with rp2040
# >>> import board
# >>> print(dir(board))
# ['__class__', '__name__', 'A0', 'A1', 'A2', 'A3', 'GP0', 'GP1', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP2', 'GP20', 'GP21', 'GP22', 'GP23', 'GP24', 'GP25', 'GP26', 'GP26_A0', 'GP27', 'GP27_A1', 'GP28', 'GP28_A2', 'GP29', 'GP29_A3', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'NEOPIXEL', 'RX', 'TX', 'UART', 'board_id']

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# keyboard.debug_enabled = True

keyboard.col_pins = (board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP29,board.GP28,board.GP27,board.GP26,board.GP15,board.GP14,board.GP13,board.GP12)
keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())
MO_1 = KC.MO(1)
LT_1_MHEN = KC.LT(1, KC.MHEN)
LT_1_HENK = KC.LT(1, KC.HENK)
LT_1_PSCR = KC.LT(1, KC.PSCR)

keyboard.keymap = [
[
	KC.TAB,  KC.Q,    KC.W,    KC.E,      KC.R,   KC.T,   KC.GRV,  KC.MINS, KC.EQL,  KC.Y,  KC.U,      KC.I,      KC.O,      KC.P,    KC.MINS, KC.BSPC,
	MO_1,    KC.A,    KC.S,    KC.D,      KC.F,   KC.G,   KC.LBRC, KC.RBRC, KC.BSLS, KC.H,  KC.J,      KC.K,      KC.L,      KC.ENT,  KC.ENT,  KC.NO,
	KC.LSFT, KC.Z,    KC.X,    KC.C,      KC.V,   KC.B,   KC.SCLN, KC.QUOT, KC.RO,   KC.N,  KC.M,      KC.COMM,   KC.DOT,    KC.SLSH, KC.RSFT, KC.UP,
	KC.LCTL, KC.LGUI, KC.LALT, LT_1_MHEN, KC.NO,  KC.NO,  KC.SPC,  KC.SPC,  KC.SPC,  KC.NO, LT_1_HENK, KC.RALT,   LT_1_PSCR, KC.LEFT, KC.DOWN, KC.RIGHT
],
[
  KC.TRNS, KC.F1,   KC.F2,   KC.F3,     KC.F4,  KC.F5,  KC.N7,   KC.N8,   KC.N9,  KC.F6,  KC.F7,     KC.F8,    KC.F9,      KC.F10,  KC.DEL,  KC.TRNS,
  KC.TRNS, KC.N1,   KC.N2,   KC.N3,     KC.N4,  KC.N5,  KC.N4,   KC.N5,   KC.N6,  KC.N6,  KC.N7,     KC.N8,    KC.N9,      KC.N0,   KC.TRNS, KC.TRNS,
  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,KC.TRNS,KC.N1,   KC.N2,   KC.N3,  KC.TRNS,KC.TRNS,   KC.TRNS,  KC.TRNS,    KC.TRNS, KC.TRNS, KC.PGUP,
  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,KC.TRNS,KC.TRNS, KC.N0,   KC.TRNS,KC.TRNS,KC.TRNS,   KC.TRNS,  KC.TRNS,    KC.HOME, KC.PGDN, KC.END
]
]

if __name__ == '__main__':
	keyboard.go()
