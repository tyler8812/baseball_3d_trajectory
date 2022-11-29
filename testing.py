import numpy as np
import cv2
import os
import sys
import numpy

numpy.set_printoptions(threshold=sys.maxsize)


a = np.load(
    "./input_file/2022-11-22-6-2/2022-11-22-6-2_coordinate.npy", allow_pickle=True
)
print(a)
# image = cv2.imread("./input_file/2022-11-22-3-1/frame0.png")

# with open(os.path.join("./input_file/2022-11-22-3-1/labels/2022-11-22-3-1_1.txt"), "r") as f:  # open in readonly mode
#     balls = f.readlines()
#     for ball in balls:
#         print(ball)
#         split_string = ball.split("\n")[0].split(" ")
#         image = cv2.circle(image, (int(split_string[1]), int(split_string[2])), 4, (255,0,0),-1)
#         image = cv2.circle(image, (int(split_string[3]), int(split_string[4])), 4, (0,255,0),-1)
#     cv2.imshow("image", image)

# cv2.waitKey(0)


# cap = cv2.VideoCapture("./input_file/2022-11-22-3-1/2022-11-22-3-1-yolo.MP4")

# while cap.isOpened():
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     cv2.line(frame, (a[3][0], a[0][1]), (a[1][0], a[0][1]), (0, 0, 255), 5)
#     cv2.line(frame, (a[1][0], a[0][1]), (a[1][0], a[2][1]), (0, 0, 255), 5)
#     cv2.line(frame, (a[1][0], a[2][1]), (a[3][0], a[2][1]), (0, 0, 255), 5)
#     cv2.line(frame, (a[3][0], a[2][1]), (a[3][0], a[0][1]), (0, 0, 255), 5)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(100) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


# b = np.load("./input_file/2022-11-22-6-2/labels.npy", allow_pickle=True)

# cap = cv2.VideoCapture("./input_file/2022-11-22-6-2/2022-11-22-6-2.MP4")
# # print(a)
# i = 0
# while cap.isOpened():
#     ret, frame = cap.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break

#     if len(b[i]) != 0:
#         print(b[i])
#         print((int(b[i][0][2][0]), int(b[i][0][2][1])))
#         frame = cv2.circle(
#             frame, (int(b[i][0][2][0]), int(b[i][0][2][1])), 10, (0, 0, 255), -1
#         )
#     cv2.imshow("frame", frame)
#     i += 1
#     if cv2.waitKey(100) == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()
