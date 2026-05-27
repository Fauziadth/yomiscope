import ctypes
import mss
import numpy as np
import cv2
import pytesseract
import time

from dotenv import load_dotenv
from config import TESSERACT_PATH

from region_selector import select_region
from region_loader import load_region, save_region

ctypes.windll.user32.SetProcessDPIAware()

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

region = load_region()

if region is None:
    region = select_region()
    save_region(region)
previous_text = ""

while True:

    with mss.mss() as sct:

        screenshot = sct.grab(region)

        img = np.array(screenshot)
        gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

        gray = cv2.resize(gray, None, fx=2, fy=2)

        # _, gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        text = pytesseract.image_to_string(gray , lang="jpn").strip()
        # if text and text != previous_text:
        print(text)
            # previous_text = text

    cv2.imshow("capture", gray)

    key = cv2.waitKey(2000)

    # Q = quit
    if key == ord("q"):
        break

    # R = reselect region
    elif key == ord("r"):

        region = select_region()
        save_region(region)

        print("New region:", region)
