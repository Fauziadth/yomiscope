import mss
import numpy as np
import cv2
from dotenv import load_dotenv
import pytesseract
from config import TESSERACT_PATH

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

with mss.mss() as sct:

    monitor = sct.monitors[1]
    screenshot = sct.grab(monitor)

    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    text = pytesseract.image_to_string(img, lang="jpn")

    print(text)