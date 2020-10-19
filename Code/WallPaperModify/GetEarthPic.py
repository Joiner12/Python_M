# -*- coding:utf-8 -*-

"""
    获取卫星图设置为桌面背景
    1.下载保存壁纸;
    2.设置为电脑壁纸;
    3.定时运行;
"""
import win32api
import win32con
import win32gui
from os import path, mkdir
from random import randint
import datetime
import requests
import time
# import urllib


def GetEerthImg(cache_dir=r'C:\Users\10520\Desktop\deskcache'):
    if not path.exists(cache_dir):
        mkdir(cache_dir)
    url_base = 'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/'
    date = datetime.datetime.utcnow().strftime('%Y/%m/%d/')
    # 卫星图更新到网站上是有时延的
    hour = str(int(datetime.datetime.utcnow().strftime('%H')) - 1).zfill(2)
    minute = str(datetime.datetime.utcnow().strftime('%M'))[0] + '0'
    second = '00'
    ext = '_0_0.png'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    picture_url = url_base + date + hour + minute + second + ext
    print(picture_url)
    res = requests.get(picture_url, headers=headers)

    with open(path.join(cache_dir, 'cache_wallpaper.png'), 'wb') as f:
        for chunk in res.iter_content():
            f.write(chunk)


def setWallpaper(image_path, wpStyle=0, tlStyle=2):
    key = win32api.RegOpenKeyEx(
        win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle",
                           wpStyle, win32con.REG_SZ, str(tlStyle))
    win32api.RegSetValueEx(key, "TileWallpaper", 0,
                           win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(
        win32con.SPI_SETDESKWALLPAPER, image_path, 1+2)


def TestSetWallpaper():
    img_path = r'D:\壁纸'
    if True and False:
        if randint(1, 10) > 5:
            img_name = r'WallPaper_2.jpg'
        else:
            img_name = r'WallPaper_7.jpg'
        img = path.join(img_path, img_name)
    else:
        img = r'C:\Users\10520\Desktop\120000_0_0.png'
    print(img)
    debugline = 1
    for i in range(3):
        for j in range(3):
            time.sleep(1)
            try:
                setWallpaper(img, wpStyle=i)
            except:
                print('set wallpaper failed')


if __name__ == "__main__":
    # GetEerthImg()
    TestSetWallpaper()
