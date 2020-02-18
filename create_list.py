
# Author: Kareza
# Created by: January 6, 2020
# Example: python3 create_list.py ./image .jpg train

import fnmatch
import os
import pandas as pd
import numpy as np 
import sys

file_path = sys.argv[1]
file_type_name = sys.argv[2]
out_file_name = sys.argv[3]

# 获取所有.file_type_name文件名称
def GetTxtName(file_path, file_type_name):
    listName = []
    for fileName in os.listdir(file_path):  
        if os.path.splitext(fileName)[1] == file_type_name:
            fileName = os.path.splitext(fileName)[0] + os.path.splitext(fileName)[1]
            listName.append(fileName)
    return listName

def ReadSaveAddr(file_path, file_type_name):
    print("Read : ",file_path)
    a_list = GetTxtName(file_path, file_type_name)
    print("Find = ",len(a_list))
    df = pd.DataFrame(np.arange(len(a_list)).reshape((len(a_list),1)),columns=['Addr']) 
    df.Addr = a_list
    print(df.head())
    df.to_csv(out_file_name + '.txt',columns=['Addr'],index=False,header=False)
    print("Write To " + out_file_name + ".txt !")
 
ReadSaveAddr(file_path, file_type_name)
