# 批量删除文件名中的str

import os
import sys

if __name__ == "__main__":
    str = input("请输入你要批量删除文件名中的字符串：")
    old_names = os.listdir()
    for old_name in old_names:
        if old_name.find(str):
            os.rename(old_name, old_name.replace(str,''))
