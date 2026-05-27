import ctypes
import mss
import numpy as np
import cv2
import pytesseract

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

while True:

    with mss.mss() as sct:

        screenshot = sct.grab(region)

        img = np.array(screenshot)
        gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

        # text = pytesseract.image_to_string(gray , lang="jpn")
        # print(text)

    cv2.imshow("capture", gray)

    key = cv2.waitKey(1)

    # Q = quit
    if key == ord("q"):
        break

    # R = reselect region
    elif key == ord("r"):

        region = select_region()
        save_region(region)

        print("New region:", region)
