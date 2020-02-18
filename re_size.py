# Author: kareza
# Create time: Feberury 18,2020
# Fuction: modify the size of all pictures in a directory.
# Example: python3 re_size.py ./image .png 640 640 ./image_640_640

import fnmatch
import os
import sys
from PIL import Image

OLD_FILE_PATH = sys.argv[1]
OLD_FILE_TYPE = sys.argv[2]
NEW_FILE_LENGTH = sys.argv[3]
NEW_FILE_WIDTH = sys.argv[4]
NEW_FILE_PATH = sys.argv[5]

def ModifyFilesName(old_file_path, old_file_type, new_file_length, new_file_width, new_file_path):
    for fileName in os.listdir(old_file_path):
        if os.path.splitext(fileName)[1] == old_file_type:
            old_im = Image.open(old_file_path + '/' +fileName)
            old_im_size = old_im.size
            print("图片宽度和高度分别是{}".format(old_im_size))
            new_im = old_im.resize((640,640))
            new_im.save(new_file_path + '/' + fileName)
    return None

if __name__ == '__main__':
    ModifyFilesName(OLD_FILE_PATH, OLD_FILE_TYPE, NEW_FILE_LENGTH, NEW_FILE_WIDTH, NEW_FILE_PATH)