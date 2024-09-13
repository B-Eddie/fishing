import pyautogui
import time
import cv2
import mss
import numpy
import pytesseract

timesleep = input("what is the cooldown: ")
# pyautogui.alert("HI")
mon = {'top': 50, 
       'left': 900, 
       'width': 500, 
       'height': 500}


def check():
    im = numpy.asarray(mss.mss().grab(mon))

    text = pytesseract.image_to_string(im)
    if "/verify" in text:
        return True
    return False
    # cv2.imshow('Image', im)

    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()

time.sleep(2)
while True:
    if check():
        # print("dnoe")
        exit()
    else:
        # print("writing")
        pyautogui.typewrite('/fish\n\n')
        time.sleep(timesleep)