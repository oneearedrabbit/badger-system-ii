import badger2040
import badger_os
from widgets import draw_window, pprint, button, wait_for_user_to_release_buttons, draw_ui

# Reduce clock speed to 48MHz
badger2040.system_speed(badger2040.SYSTEM_NORMAL)

changed = False
exited_to_launcher = False
woken_by_button = badger2040.woken_by_button()  # Must be done before we clear_pressed_to_wake

if badger2040.pressed_to_wake(badger2040.BUTTON_A) and badger2040.pressed_to_wake(badger2040.BUTTON_C):
    # Pressing A and C together at start quits app
    exited_to_launcher = badger_os.state_clear_running()
else:
    # Otherwise restore previously running app
    badger_os.state_launch()

display = badger2040.Badger2040()
display.led(128)

state = {
    "running": "launcher",
}

badger_os.state_load("launcher", state)

def draw_about():
    x = 78
    y = 39
    width = 144
    height = 63
    draw_window(display, x, y, width, height, " Welcome ")
        
    # logo
    image = bytearray(int(32 * 32 / 8))
    open("images/{}".format("census.bin"), "r").readinto(image)
    display.image(image, 32, 32, 86, 56)    

    pprint(display, "Engineering", 125, 56, 0)
    pprint(display, "Offsite", 125, 66, 0)
    pprint(display, "Brooklyn", 125, 76, 0)
    pprint(display, "2022", 125, 86, 0)

def render():
    display.pen(15)
    display.clear()
    
    draw_ui(display, "About")
    
    draw_about()
        
    display.update()
    
if exited_to_launcher or not woken_by_button:
    wait_for_user_to_release_buttons(display)
    display.update_speed(badger2040.UPDATE_NORMAL)
    render()
    display.led(0)

display.update_speed(badger2040.UPDATE_NORMAL)

# Save power, do NOT render screen every time
while True:        
    if display.pressed(badger2040.BUTTON_A):
        changed = True
        button(display, badger2040.BUTTON_A)
    if display.pressed(badger2040.BUTTON_B):
        changed = True
        button(display, badger2040.BUTTON_B)
    if display.pressed(badger2040.BUTTON_C):
        changed = True
        button(display, badger2040.BUTTON_C)

#     if display.pressed(badger2040.BUTTON_UP):
#         button(display, badger2040.BUTTON_UP)
#     if display.pressed(badger2040.BUTTON_DOWN):
#         button(display, badger2040.BUTTON_DOWN)

    if changed:
        badger_os.state_save("launcher", state)
        changed = False
        
    # Halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()

