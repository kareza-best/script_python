# Author: kareza
# Create time: February 18,2020
# Fuction: Bulk delete specified string in filename.
# Example: python3 re_name.py ./mask_640_640 _seg0
import os
import sys

FILE_PATH = sys.argv[1]
STR = sys.argv[2]

if __name__ == "__main__":
    old_names = os.listdir(FILE_PATH)
    for old_name in old_names:
        if old_name.find(STR):
            os.rename(FILE_PATH + '/' +old_name, FILE_PATH + '/' + old_name.replace(STR,''))
