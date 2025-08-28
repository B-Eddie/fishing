import pyautogui
import time

# Delay to give you time to switch to the target application
time.sleep(2)

while True:
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')
    time.sleep(2)