# importing the module
import cv2
import argparse
from pathlib import Path
import numpy as np
import os


def convert_xyxy_to_middle(string):
    top_x = int(string[1])

    top_y = int(string[2])
    down_x = int(string[3])
    down_y = int(string[4])
    middle_x = (top_x + down_x) // 2
    middle_y = (top_y + down_y) // 2
    return (middle_x, middle_y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_folder", type=str, help="input")
    parser.add_argument("--output", type=str, help="output")
    parser.add_argument("--input_video", type=str, help="length of video")
    parser.add_argument("--video_name", type=str, help="name of video")
    parser.add_argument("--view", type=int, help="name of video")
    args = parser.parse_args()

    import cv2

    cap = cv2.VideoCapture(args.input_video)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("\n----------------------------------------\n")
    print(f"{args.video_name}: {length} frames")
    print("\n----------------------------------------\n")
    result = []
    for i in range(1, length + 1):
        current_ball = []
        if os.path.isfile(args.input_folder + f"/{args.video_name}_{i}.txt"):
            with open(
                os.path.join(args.input_folder + f"/{args.video_name}_{i}.txt"), "r"
            ) as f:  # open in readonly mode
                balls = f.readlines()
                for ball in balls:
                    split_string = ball.split("\n")[0].split(" ")
                    middle_point = convert_xyxy_to_middle(split_string)
                    confidence_score = float(split_string[5])
                    # Todo
                    # if args.view == 2:
                    #     # too right
                    #     if int(split_string[1]) > 1100:
                    #         continue
                    #     # too left
                    #     if int(split_string[3]) < 516:
                    #         continue
                    #     # too top
                    #     if int(split_string[4]) < 387:
                    #         continue
                    #     # too low
                    #     if int(split_string[2]) > 820:
                    #         continue

                    # else:
                    #     # too right
                    #     if int(split_string[1]) > 1247:
                    #         continue
                    #     # too left
                    #     if int(split_string[3]) < 843:
                    #         continue
                    #     # too top
                    #     if int(split_string[4]) < 300:
                    #         continue
                    #     # too low
                    #     if int(split_string[2]) > 775:
                    #         continue

                    current_ball.append([confidence_score, middle_point])

        result.append(current_ball)

        np.save(args.output, result)
