import cv2
import numpy as np
import mss

start_point = None
end_point = None
drawing = False


def mouse_callback(event, x, y, flags, param):
    global start_point, end_point, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        end_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)


def select_region():

    global start_point, end_point

    with mss.mss() as sct:

        monitor = sct.monitors[0]
        screenshot = np.array(sct.grab(monitor))

    img = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    clone = img.copy()

    cv2.namedWindow("Select Region", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Select Region", mouse_callback)

    while True:

        temp = clone.copy()

        if start_point and end_point:
            cv2.rectangle(temp, start_point, end_point, (0,255,0), 2)

        cv2.imshow("Select Region", temp)

        key = cv2.waitKey(1)

        if key == 13:
            break

    cv2.destroyAllWindows()

    x1, y1 = start_point
    x2, y2 = end_point

    region = {
        "top": min(y1, y2) + monitor["top"],
        "left": min(x1, x2) + monitor["left"],
        "width": abs(x2 - x1),
        "height": abs(y2 - y1),
    }

    return region