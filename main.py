from kmk.extensions.lock_status import LockStatus
from kmk.modules.layers import Layers
from kmk.keys import KC
from rgb_patched import RGB, AnimationModes
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.extensions import lock_status

import digitalio
import board

from kb import KMKKeyboard

print("Starting")

keyboard = KMKKeyboard()

# rgb
#class AnimationModes:
#    OFF = 0
#    STATIC = 1
#    STATIC_STANDBY = 2
#    BREATHING = 3
#    RAINBOW = 4
#    BREATHING_RAINBOW = 5
#    KNIGHT = 6
#    SWIRL = 7
#    USER = 8

rgb_ext = RGB(
    pixel_pin=board.GP28,
    num_pixels=16,
    val_limit=100,
    val_default=25,
    animation_mode=AnimationModes.BREATHING_RAINBOW,
    animation_speed = 2
)
keyboard.extensions.append(rgb_ext)


# led mappings
INACTIVE = False
ACTIVE = True

# for some reason this has to be set to disabled led at start

keyboard.modules = [
    Layers(),
]

# Keys mapping
SUPER = KC.LWIN
SHIFT = KC.LSHIFT
RSHIFT = KC.RSHIFT
LCTRL = KC.LCTRL
RCTRL = KC.RCTRL
ALT = KC.LALT
RALT = KC.RALT
TAB = KC.TAB
ESC = KC.ESCAPE
ENTER = KC.ENTER
SPACE = KC.SPACE
BACK = KC.BACKSPACE
DEL = KC.DELETE
# CAPS = KC.CAPS
CAPS = SUPER

XX = KC.NO
NONE = XX
TO_CHECK = XX
___ = XX
TRANS = KC.TRANSPARENT

# Layers 
L0 = KC.TO(0)	
L1 = KC.TT(1)
L2 = KC.TT(2)

# Settings
keyboard.tap_time = 250
keyboard.debug_enabled = False 

# keymap
keyboard.keymap = [
    [
        ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BACKSPACE,
        TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, ENTER, 
        SUPER, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SEMICOLON, KC.QUOTE, KC.SLASH,
        ___, SHIFT, KC.ZKHK, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.BSLASH, KC.RSHIFT,
        ___, LCTRL, ___, SUPER, KC.LALT,  ___, ___, KC.SPACE,  ___, ___, ___, RALT, L1, L2, RCTRL, 
    ],
    [
        TRANS, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, TRANS, 
        TRANS, KC.RGB_ANI, KC.RGB_AND, KC.E, KC.R, KC.T, KC.PGUP, KC.UP, KC.PGDN, DEL, KC.P, KC.LBRACKET, KC.RBRACKET, ENTER, 
        TRANS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.LEFT, KC.DOWN, KC.RIGHT, KC.L, KC.SEMICOLON, KC.QUOTE, KC.SLASH,
        ___, TRANS, TRANS, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.HOME, KC.END, TRANS, TRANS, KC.BSLASH, KC.RSHIFT,
        ___, TRANS, ___, TRANS, TRANS,  ___, ___, TRANS,  ___, ___, ___, TRANS, L0, L2, TRANS, 

    ],
    [
        KC.RGB_TOG, KC.RGB_MODE_PLAIN, KC.RGB_MODE_BREATHE, KC.RGB_MODE_RAINBOW, KC.RGB_MODE_BREATHE_RAINBOW, KC.RGB_MODE_KNIGHT, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, TRANS, 
        TRANS, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.PGUP, KC.UP, KC.PGDN, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, ENTER, 
        TRANS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.LEFT, KC.DOWN, KC.RIGHT, KC.L, KC.SEMICOLON, KC.QUOTE, KC.SLASH,
        ___, TRANS, TRANS, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.HOME, KC.END, TRANS, TRANS, KC.BSLASH, KC.RSHIFT,
        ___, TRANS, ___, TRANS, TRANS,  ___, ___, TRANS,  ___, ___, ___, TRANS, L0, L1, TRANS, 
    ]
]

if __name__ == '__main__':
    keyboard.go()
