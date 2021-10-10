import cv2
import numpy as np
import os


def process_image(file_path, target_dir):
    pic = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    x, y = pic.shape[0:2]
    pic1 = cv2.resize(pic, (int(y/2), int(x/2)))
    file_name = file_path.split("/")[-1]
    cv2.imwrite(os.path.join(target_dir, file_name), pic1)


root, dirs, files = next(os.walk("tips_3/"))
for item in files:
    file_path = os.path.join(root, item)
    process_image(file_path, "tips_3_resize")
