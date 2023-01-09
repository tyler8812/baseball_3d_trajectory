import numpy as np
import cv2
import os
import sys
import numpy

# numpy.set_printoptions(threshold=sys.maxsize)

# image = cv2.imread("./input_file/2022-12-19-4-1/2022-12-19-4-1_poly.png")
# image = image * 255
# cv2.imshow("image", image)
# cv2.waitKey(0)

import copy

# play video
cap = cv2.VideoCapture("./video/2022-12-19-4-2.MP4")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)
        key = cv2.waitKey(10)

        if key == ord("q") or key == 27:  # q or esc
            break
        elif key == 13:  # enter
            background = copy.deepcopy(frame)

            overlay = cv2.imread("./input_file/2022-12-19-4-2/2022-12-19-4-2_poly.png")
            overlay = overlay * 255
            added_image = cv2.addWeighted(background, 0.8, overlay, 0.5, 0)

            cv2.imshow("check", added_image)
