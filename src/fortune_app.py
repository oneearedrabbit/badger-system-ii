import badger2040
import os
import badger_os
from widgets import draw_window, pprint, ptitle, plength, ppara, button, draw_ui
from random import random

IMAGE_WIDTH = 96
IMAGE_HEIGHT = 96
DELTA = 0

# Check that the fortune directory exists, if not, make it
try:
    os.mkdir("fortune")
except OSError:
    pass

display = badger2040.Badger2040()
display.update_speed(badger2040.UPDATE_FAST)

file = "cookie.txt"
cookies = open("fortune/cookie.txt", "r").read().split("%\n")
total_cookies = len(cookies)

state = {
    "running": "badge_app",
}

IMAGE_WIDTH = 64
IMAGE_HEIGHT = 64

def render():
    display.pen(15)
    display.thickness(1)
    display.rectangle(12, 42, 222, 84)
    
    display.pen(0)
    display.thickness(1)
    n = int(random()*total_cookies)
    print(f"Quote {n}")
    text = cookies[n].strip().replace("\n", " ").replace("\t\t", " ").replace("\t", " ")

    ppara(display, text, 12, 42, 222, 0)
    display.update()

def draw_clippy():
    x = 1
    y = 21
    width = 294
    height = 106
    draw_window(display, x, y, width, height, " Special ")

    clippy_dat = bytearray(int(IMAGE_WIDTH * IMAGE_HEIGHT / 8))
    open(f"images/clippy.bin", "rb").readinto(clippy_dat)
    display.image(clippy_dat, IMAGE_WIDTH, IMAGE_HEIGHT, 212, 56)

    # scrollbars
    display.pen(0)
    display.thickness(1)
    scroll_size = 14
    title_height = 11
    display.rectangle(x + width - scroll_size - 1, y + title_height, scroll_size + 1, scroll_size)
    display.rectangle(x + width - scroll_size - 1, y + height - scroll_size, scroll_size + 1, scroll_size)
    display.rectangle(x + width - scroll_size - 1, y + title_height + scroll_size, scroll_size + 1, height - title_height)

    display.pen(15)
    display.rectangle(x + width - scroll_size, y + title_height + 1, scroll_size - 1, scroll_size - 2)
    display.rectangle(x + width - scroll_size, y + height - scroll_size + 1, scroll_size - 1, scroll_size - 2)
    display.pen(12)
    display.rectangle(x + width - scroll_size, y + title_height + scroll_size, scroll_size - 1, height - 2 * scroll_size - title_height)

    # arrows
    display.pen(0)
    # top
    display.line(x + width - scroll_size // 2 - 1, y + title_height + 2, x + width - scroll_size // 2 - 7, y + title_height + 8)
    display.line(x + width - scroll_size // 2 - 1, y + title_height + 3, x + width - scroll_size // 2 - 6, y + title_height + 8)
    display.line(x + width - scroll_size // 2 - 1, y + title_height + 2, x + width - scroll_size // 2 + 5, y + title_height + 8)
    display.line(x + width - scroll_size // 2 - 1, y + title_height + 3, x + width - scroll_size // 2 + 4, y + title_height + 8)
    display.line(x + width - scroll_size // 2 - 4, y + title_height + 7, x + width - scroll_size // 2 - 4, y + title_height + 12)
    display.line(x + width - scroll_size // 2 + 2, y + title_height + 7, x + width - scroll_size // 2 + 2, y + title_height + 12)
    display.line(x + width - scroll_size // 2 - 4, y + title_height + 11, x + width - scroll_size // 2 + 3, y + title_height + 11)
    
    # bottom
    display.line(x + width - scroll_size // 2 - 1, y + height - 3, x + width - scroll_size // 2 - 7, y + height - 9)
    display.line(x + width - scroll_size // 2 - 1, y + height - 4, x + width - scroll_size // 2 - 6, y + height - 9)
    display.line(x + width - scroll_size // 2 - 1, y + height - 3, x + width - scroll_size // 2 + 5, y + height - 9)
    display.line(x + width - scroll_size // 2 - 1, y + height - 4, x + width - scroll_size // 2 + 4, y + height - 9)
    display.line(x + width - scroll_size // 2 - 4, y + height - 8, x + width - scroll_size // 2 - 4, y + height - 13)
    display.line(x + width - scroll_size // 2 + 2, y + height - 8, x + width - scroll_size // 2 + 2, y + height - 13)
    display.line(x + width - scroll_size // 2 - 4, y + height - 12, x + width - scroll_size // 2 + 3, y + height - 12)

def draw_elements():
    display.pen(15)
    display.clear()

    draw_ui(display, "Special")
    
    draw_clippy()

changed = not badger2040.woken_by_button()

draw_elements()

while True:
    if display.pressed(badger2040.BUTTON_A):
        changed = True
        button(display, badger2040.BUTTON_A)
    if display.pressed(badger2040.BUTTON_B):
        changed = True
        button(display, badger2040.BUTTON_B)
    if display.pressed(badger2040.BUTTON_C) or display.pressed(badger2040.BUTTON_UP) or display.pressed(badger2040.BUTTON_DOWN):
        changed = True
#         button(display, badger2040.BUTTON_C)
        
    if changed:
        display.led(128)
        render()
        badger_os.state_save("fortune", state)
        display.led(0)
        changed = False

    display.halt()
