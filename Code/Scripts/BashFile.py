# -*- coding:utf-8 -*-

import os
import shutil


def BashFile():
    tar_path = r"C:\Users\Whtest\Desktop\Draft"
    # listdir function
    detail = os.listdir(tar_path)
    if len(detail) > 0:
        for i in detail:
            pass
            # print(i)
    # walk function
    detail_1 = os.walk(tar_path)
    for (path, dirnames, filenames) in detail_1:
        for i in dirnames:
            print(i)
        for j in filenames:
            print(j)


if __name__ == "__main__":
    print("bash file handle")
    BashFile()
