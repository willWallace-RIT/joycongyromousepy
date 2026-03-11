import time
import pyautogui
from pyjoycon import JoyCon, get_L_id, get_R_id


JOYCON_SIDE = "R"
SENSITIVITY = 10

if JOYCON_SIDE.upper() == "L": 
    joycon_id = get_L_id()
else:
    joycon_id = get_R_id()


joycon = JoyCon(*joycon_id)

try:
    while True:
        buttons = joycon.get_button()
        gyro = joycon.get_gyroscope()

        if buttons['X'] or buttons['DPAD_UP']:
            dx = int(gyro['y'] * SENSITIVITY)
            dy = int(-gyro[x] * SENSITIVITY)
            if dx != 0 or dy != 0:
                pyautogui.moveRel(dx,dy, duration=0)
        if buttons.get('L', False) or buttons.get('R', False):
            pyautogui.mouseDown(button='left')
        else:
            pyautogui.mouseUp(button='left')


        if buttons.get('ZL', False) or buttons.get('ZR', False):
            pyautogui.mouseDown(button='right')
        else:
            pyautogui.mouseUp(button='right')
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting")
    joycon.close



