import badger2040
import qrcode
import os
import badger_os
from widgets import draw_window, pprint, ptitle, plength, button, draw_ui

# Check that the qrcodes directory exists, if not, make it
try:
    os.mkdir("qrcodes")
except OSError:
    pass

# Load all available QR Code Files
try:
    CODES = [f for f in os.listdir("/qrcodes") if f.endswith(".txt")]
    TOTAL_CODES = len(CODES)
except OSError:
    pass


print(f'There are {TOTAL_CODES} QR Codes available:')
for codename in CODES:
    print(f'File: {codename}')

display = badger2040.Badger2040()

code = qrcode.QRCode()


state = {
    "running": "qr_app",
    "current_qr": 0
}


def measure_qr_code(size, code):
    w, h = code.get_size()
    module_size = int(size / w)
    return module_size * w, module_size


def draw_qr_code(ox, oy, size, code):
    size, module_size = measure_qr_code(size, code)
    display.pen(15)
    display.rectangle(ox, oy, size, size)
    display.pen(0)
    for x in range(size):
        for y in range(size):
            if code.get_module(x, y):
                display.rectangle(ox + x * module_size, oy + y * module_size, module_size, module_size)


def draw_qr_file(n):
    draw_window(display, 6, 26, 282, 94, " About us ")

    file = CODES[n]
    codetext = open("qrcodes/{}".format(file), "r")

    lines = codetext.read().strip().split("\n")
    code_text = lines.pop(0)
    title_text = lines.pop(0)
    detail_text = lines

    display.pen(0)

    code.set_text(code_text)
    size, _ = measure_qr_code(128, code)
    draw_qr_code(10, 41, 80, code)

    left = 96

    display.thickness(2)
    ptitle(display, title_text, left, 40, 0)
    display.thickness(1)

    top = 56
    for line in detail_text:
        pprint(display, line, left, top, 0)
        top += 10

    if TOTAL_CODES > 1:
        for i in range(TOTAL_CODES):
            x = 286
            y = int((128 / 2) - (TOTAL_CODES * 10 / 2) + (i * 10))
            display.pen(0)
            display.rectangle(x, y, 8, 8)
            if state["current_qr"] != i:
                display.pen(15)
                display.rectangle(x + 1, y + 1, 6, 6)

def render():
    display.pen(15)
    display.clear()

    draw_ui(display, "QR")
    
    draw_qr_file(state["current_qr"])
    
    display.update()

badger_os.state_load("qrcodes", state)
changed = not badger2040.woken_by_button()

while True:
    if TOTAL_CODES > 1:
        if display.pressed(badger2040.BUTTON_UP):
            if state["current_qr"] > 0:
                state["current_qr"] -= 1
                changed = True

        if display.pressed(badger2040.BUTTON_DOWN):
            if state["current_qr"] < TOTAL_CODES - 1:
                state["current_qr"] += 1
                changed = True

    if display.pressed(badger2040.BUTTON_A):
        changed = True
        button(display, badger2040.BUTTON_A)
    if display.pressed(badger2040.BUTTON_B):
        changed = True
#         button(display, badger2040.BUTTON_B)
    if display.pressed(badger2040.BUTTON_C):
        changed = True
        button(display, badger2040.BUTTON_C)
    
    if changed:
        display.led(128)
        render()
        badger_os.state_save("qrcodes", state)
        display.led(0)
        changed = False

    # Halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()
