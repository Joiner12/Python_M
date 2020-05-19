# -*- coding:utf-8 -*-


__author__ = "Risky Junior"
__date__ = "2020年5月19日"

from os import path, listdir, walk


class RegularWallPaper():
    img_Format = ['.jpg', '.jpeg', '.bpm', '.png']
    img_files = list()
    img_fullfile = list()

    def __init__(self, filepath=r"D:\壁纸-1"):
        self.filepath = filepath
        self.img_files = list()
        self.img_fullfile = list()
        self.RFlag = False

        if path.isdir(filepath):
            print("input dir exists")
        else:
            print("input file path:%s is not exist,check it\n" % (filepath))
            return None
        self.GetImagePath()

    def GetImagePath(self):
        for root, dir, files in walk(self.filepath):
            for j in files:
                if path.splitext(j)[1] in self.img_Format:
                    self.img_files.append(j)
                    self.img_fullfile.append(path.join(root, j))

    def CheckFileName(self, standardPrefix="Wallpaper_"):
        if len(self.img_files) == 0:
            return
        for img in self.img_files:
            print(img)


if __name__ == "__main__":
    ex = RegularWallPaper()
    debug_tag = 0
