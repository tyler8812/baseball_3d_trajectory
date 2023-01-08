# Import necessary libraries
import cv2
import numpy as np
import argparse
import sys

# np.set_printoptions(threshold=sys.maxsize)


def draw_poly_and_save(img, coordinate_list):
    print("saving to " + str(Path(args.output)))
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    points = np.array(coordinate_list)
    cv2.fillPoly(blank_image, pts=[points], color=(255, 255, 255))
    blank_image = blank_image / 255
    cv2.imwrite(str(Path(args.output)), blank_image)
    print(np.sum(blank_image))


def draw_img(coordinate_list, img):
    circle_color = (255, 0, 0)
    img_draw = copy.deepcopy(img)
    for i, (x, y) in enumerate(coordinate_list):
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.circle(img_draw, (x, y), 1, circle_color, -1)
        # cv2.circle(img_draw, (x, y), 5, circle_color, 2)
        # cv2.putText(
        #     img_draw,
        #     "{}: x:{}, y:{}".format(str(i), str(x), str(y)),
        #     (x + 20, y + 20),
        #     font,
        #     1,
        #     (255, 0, 0),
        #     2,
        # )
    cv2.imshow("check", img_draw)
    return img_draw


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # img_prev = copy.deepcopy(img)

        # displaying the coordinates
        # on the Shell
        print(x, " ", y)

        coordinate_list.append([x, y])
        # draw_img()
        draw_img(coordinate_list, img)


if __name__ == "__main__":
    from pathlib import Path
    import copy
    import numpy as np

    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=str, help="source video")
    parser.add_argument(
        "--output", type=str, default="coordinate.npy", help="<ref_point.npy>"
    )
    args = parser.parse_args()

    coordinate_list = []

    # play video
    cap = cv2.VideoCapture(str(Path(args.video)))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow("frame", frame)
            key = cv2.waitKey(10)
            if key == ord("q") or key == 27:  # q or esc
                break
            elif key == 13:  # enter
                img = copy.deepcopy(frame)
                cv2.imshow("check", img)
                # setting mouse handler for the image
                # and calling the click_event() function
                cv2.setMouseCallback("check", click_event)

                # wait for a key to be pressed to exit
                while True:
                    key = cv2.waitKey(0)
                    if key == ord("x") and len(coordinate_list) > 0:
                        coordinate_list.pop()
                        draw_img(coordinate_list, img)
                    elif key == ord("a") and len(coordinate_list) > 0:
                        coordinate = coordinate_list.pop()
                        coordinate_list.append([coordinate[0] - 1, coordinate[1]])
                        draw_img(coordinate_list, img)
                    elif key == ord("w") and len(coordinate_list) > 0:
                        coordinate = coordinate_list.pop()
                        coordinate_list.append([coordinate[0], coordinate[1] - 1])
                        draw_img(coordinate_list, img)
                    elif key == ord("d") and len(coordinate_list) > 0:
                        coordinate = coordinate_list.pop()
                        coordinate_list.append([coordinate[0] + 1, coordinate[1]])
                        draw_img(coordinate_list, img)
                    elif key == ord("s") and len(coordinate_list) > 0:
                        coordinate = coordinate_list.pop()
                        coordinate_list.append([coordinate[0], coordinate[1] + 1])
                        draw_img(coordinate_list, img)
                    elif key == 27:
                        break
                    elif key == ord("z"):
                        draw_poly_and_save(img, coordinate_list)

                        break

    # close the window
    cv2.destroyAllWindows()
