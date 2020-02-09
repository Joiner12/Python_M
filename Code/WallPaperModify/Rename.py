# -*- coding:utf-8 -*-

'''
    Script Name:Rename.py
    Description:
    1.重命名壁纸文件（D:\壁纸 - 副本）
    2.将脚本打包成exe文件

    reference:
    [1] <os库>https://docs.python.org/zh-cn/3/library/os.html
    [2] <os库常用函数>https://www.jianshu.com/p/812fd4d0d71d
    [3] <split函数>https://blog.csdn.net/ydyang1126/article/details/75050175
    [4] <字符串>https://www.runoob.com/python/python-strings.html
    [5] <break|return>https://stackoverflow.com/questions/28854988/what-is-the-difference-between-return-and-break-in-python
    [6] <数据类型转换>https://www.cnblogs.com/shockerli/p/python3-data-type-convert.html
'''

import os
import shutil


def Re_WallPaper():
    filepath = r"D:\壁纸 - 副本"
    std_name = r'Wallpaper_'
    fileCnt = 0
    if CheckName(filepath, std_name):
        print(' start to rename')
        # rename
        detail_2 = os.listdir(filepath)
        picsTemp = []

        for file_1 in detail_2:
            sepNameTemp = SeperateName(file_1)
            pic_Format = ['png', 'gif', 'jpg', 'bpm']
            if pic_Format.count(sepNameTemp[1]) != 0:
                os.rename(file_1, std_name+str(fileCnt)+sepNameTemp[1])
                fileCnt = fileCnt + 1
            else:
                pass
    else:
        print('no need to rename handle')
    debug_a = 1
    print(fileCnt, 'file rename finished')


def SeperateName(origin_name):
    if isinstance(origin_name, str):
        splt_str = origin_name.split('.', 1)
        out_name = splt_str
        return out_name
    else:
        return ''


'''
是否需要启动重命名
'''


def CheckName(filepath, std_name):
    renameFlag = False
    detail_1 = os.listdir(filepath)

    for i in detail_1:
        if i.find(std_name, 1) == -1:
            # 区别是否为图片格式bmp,jpg,png,tif,gif
            SepTemp_1 = SeperateName(i)
            pic_Format = ['png', 'gif', 'jpg', 'bpm']
            if pic_Format.count(SepTemp_1[1]) != 0:
                renameFlag = True
                break
        else:
            pass
    return renameFlag


if __name__ == "__main__":
    os.system('cls')
    print('你紧紧拉住我衣袖')
    Re_WallPaper()
    # a = SeperateName('what.1')
    # print(a)
