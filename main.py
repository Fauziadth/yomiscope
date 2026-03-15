import mss
import numpy as np
import cv2
from paddleocr import PaddleOCR

# init OCR (Japanese)
# ocr = PaddleOCR(lang="japan")

with mss.mss() as sct:

    monitor = sct.monitors[1]  # main monitor

    screenshot = sct.grab(monitor)
    img = np.array(screenshot)

    # output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
    # mss.tools.to_png(screenshot.rgb, screenshot.size, output=output)


    # convert BGRA -> BGR
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # result = ocr.ocr(img)

    print("\nDetected text:\n")
    #
    # for line in result[0]:
    #     text = line[1][0]
    #     print(text)