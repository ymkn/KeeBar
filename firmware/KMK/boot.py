import board
import digitalio
import storage
import usb_cdc
import usb_hid
from kmk.kmk_keyboard import KMKKeyboard

# to enable USB storage, hold top-left key (typcally ESC key) in few seconds while connecting USB cable to your keyboard

col = digitalio.DigitalInOut(board.GP12)
row = digitalio.DigitalInOut(board.GP0)

row.switch_to_input(pull=digitalio.Pull.DOWN)
col.switch_to_output(value=True)

if not row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_hid.enable(usb_hid.Device.KEYBOARD, boot_device=1)

row.deinit()
col.deinit()