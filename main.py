import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import mss
import numpy as np
import cv2
from dotenv import load_dotenv
import pytesseract
import pyautogui
from config import TESSERACT_PATH

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

region = {'top': 980, 'left': -1269, 'width': 702, 'height': 109}

with mss.mss() as sct:
    print(sct.monitors)

    monitor = sct.monitors[0]
    screenshot = sct.grab(region)

    img = np.array(screenshot)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    cv2.imshow("capture", gray)
    cv2.waitKey(0)


    print(pyautogui.position())

    # text = pytesseract.image_to_string(gray , lang="jpn")
    #
    # print(text)