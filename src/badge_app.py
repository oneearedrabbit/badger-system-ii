import badger2040
import os
import badger_os
from widgets import draw_window, pprint, ptitle, plength, button, draw_ui

IMAGE_WIDTH = 96
IMAGE_HEIGHT = 96
DELTA = 0

# Check that the badges directory exists, if not, make it
try:
    os.mkdir("badges")
except OSError:
    pass
    
# Load all available badge Code Files
try:
    CODES = [f for f in os.listdir("/badges") if f.endswith(".txt")]
    TOTAL_CODES = len(CODES)
except OSError:
    pass

print(f'There are {TOTAL_CODES} badges available:')
for codename in CODES:
    print(f'File: {codename}')

display = badger2040.Badger2040()
display.update_speed(badger2040.UPDATE_NORMAL)

state = {
    "running": "badge_app",
}

def draw_badge(n):
    draw_window(display, 6, 26, 182, 94, " Badge ")

    file = CODES[n]
    codetext = open("badges/{}".format(file), "r")

    lines = codetext.read().strip().split("\n")
    name_text = lines.pop(0)
    title_text = lines.pop(0)
    company_text = lines.pop(0)
    github_text = lines.pop(0)
    badge_path = lines.pop(0)
    
    ptitle(display, name_text, 15, 44, 0)
    
    if len(github_text.strip()) > 0:
        # github icon
        display.image(bytearray((0x3c,0x00,0xa5,0x81,0x81,0xc3,0x66,0x84)), 8, 8, 18, 86)
        display.image(bytearray((0x00,0x00,0x00,0x00,0x00,0x00,0xfc,0xfe)), 8, 8, 18, 78)
        display.image(bytearray((0x03,0x03,0x03,0x03,0x03,0x02,0x01,0x00)), 8, 8, 10, 86)
        display.image(bytearray((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x01)), 8, 8, 10, 78)
    
    pprint(display, title_text, 15, 60, 0)
    pprint(display, company_text, 15, 72, 0)
    pprint(display, github_text, 30, 84, 0)
    
    badge_dat = bytearray(int(IMAGE_WIDTH * IMAGE_HEIGHT / 8))
    open(f"badges/{badge_path}", "rb").readinto(badge_dat)
        
    display.image(badge_dat, IMAGE_WIDTH, IMAGE_HEIGHT, 194, 26)


def render():
    display.pen(15)
    display.clear()

    draw_ui(display, "Badge")
    
    draw_badge(0)
    
    display.update()    

changed = not badger2040.woken_by_button()

while True:
    if display.pressed(badger2040.BUTTON_A):
        changed = True
#         button(display, badger2040.BUTTON_A)
    if display.pressed(badger2040.BUTTON_B):
        changed = True
        button(display, badger2040.BUTTON_B)
    if display.pressed(badger2040.BUTTON_C):
        changed = True
        button(display, badger2040.BUTTON_C)

    if changed:
        display.led(128)
        render()
        badger_os.state_save("badges", state)
        display.led(0)
        changed = False

    display.halt()
