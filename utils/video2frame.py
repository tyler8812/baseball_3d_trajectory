import cv2
from os import listdir, makedirs
from os.path import isfile, join, splitext, exists
from pathlib import Path

video_path = "./video/2022-11-22-6-2.MP4"
output_folder = "./frame"
# only for one video
file_name = Path(video_path).stem
vidcap = cv2.VideoCapture(video_path)
success, image = vidcap.read()
count = 0
if not exists(output_folder + "/" + file_name):
    makedirs(output_folder + "/" + file_name)
while success:
    cv2.imwrite(
        output_folder + "/" + file_name + "/frame%d.png" % count, image
    )  # save frame as JPEG file
    success, image = vidcap.read()
    print("Read a new frame: ", success)
    count += 1
print("total frame: {}".format(count))
