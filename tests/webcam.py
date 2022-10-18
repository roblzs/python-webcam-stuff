import cv2
import numpy as np
from test import remove_bg

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    # cv2.imshow('Input', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   

    gray_flip = cv2.flip(gray,1)

    # combined_window = np.hstack([gray,gray_flip])

    cv2.imshow("Combined videos ",gray_flip)
    key=cv2.waitKey(1)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()