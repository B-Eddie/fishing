import pyautogui
import time
import cv2
import mss
import numpy
import pytesseract
import tkinter as tk
from pynput.mouse import Listener

top_left = None
bottom_right = None
click_count = 0  # Counter to track first and second click

def on_click(x, y, button, pressed):
    global top_left, bottom_right, click_count

    if pressed:
        if click_count == 0:
            # First click: Capture the top-left corner
            top_left = (x, y)
            print(f"Top-left corner set at: {top_left}")
            click_count += 1
        elif click_count == 1:
            # Second click: Capture the bottom-right corner
            bottom_right = (x, y)
            print(f"Bottom-right corner set at: {bottom_right}")
            click_count += 1
            # Stop the listener after second click
            return False

# Initialize the main window for cooldown input
root = tk.Tk()
root.withdraw()  # Hide the root window as we don't need it

# Instructions for the user
print("Move the mouse to the top-left corner of the region and click.")

# Start mouse listener to detect the clicks
with Listener(on_click=on_click) as listener:
    listener.join()

# Wait for both clicks to be registered (top-left and bottom-right)
print("Mouse clicks captured successfully.")

# Calculate width and height from the top-left and bottom-right coordinates
left, top = top_left
right, bottom = bottom_right
width, height = right - left, bottom - top

# Ask the user for cooldown time
timesleep = float(input("Enter the cooldown time (seconds): "))

# Define the region to capture based on mouse clicks
mon = {'top': top, 'left': left, 'width': width, 'height': height}

def check():
    im = numpy.asarray(mss.mss().grab(mon))
    text = pytesseract.image_to_string(im)
    print(text)
    if "verify" in text:
        return True
    return False

# Adding a small delay to let the user prepare (optional)
print("The program will start in 2 seconds.")
time.sleep(2)

# Main loop
while True:
    if check():
        print("/verify found! Exiting.")
        exit()
    else:
        pyautogui.typewrite('/fish\n\n')
        time.sleep(timesleep)
