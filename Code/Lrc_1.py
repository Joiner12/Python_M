# -*- coding:utf-8 -*-

__author__: "Anonymous"
__date__: "2019-12-5"
import os
import re
import datetime
import random as rd
import jieba
from wordcloud import WordCloud
import turtle


'''
    遍历文件
'''

# 从单个文件中读取
def GetLrc():
    print('get lrc from file')
    file = 'xx.lrc'
    with open(file,"r",encoding="utf-8") as lrc:
        lrd_detail = lrc.readlines()
        print('lrc file open succeed')
    for piece_lrc in lrd_detail:
        piece_pattern = re.compile(r"\[.+\]")
        # print('origin:'+ piece_lrc)
        words = piece_pattern.sub(" ",piece_lrc)
        if len(words)!=0:
            print(words)
        
    lrc.close()

'''
获取文件索引
保存为D:\Python_M\Src\LRC\IndexLrc.txt
'''
def GetFileIndex():
    tarPath = r'D:\Python_M\Code'
    srcPath = r'D:\Python_M\Src\LRC'
    # (当前文件夹路径,子文件夹，当前文件夹文件)
    fileTemp = os.walk(srcPath)
   
    with open(r'D:\Python_M\Src\LRC\IndexLrc.txt',encoding='utf-8',mode='w') as indexOut:
        # 时间戳
        now = datetime.datetime.now()
        time_now = now.strftime('%a, %b %d %H:%M')
        print(time_now)
        indexOut.writelines('Created timedate:%s\n'%(time_now))
        cnt = 0
        for i in fileTemp:
            cnt += 1
            if cnt > 0:
                for j in i[2]:
                    info_temp = i[0] + '\\' + j
                    print(info_temp,j)
                    indexOut.writelines('%s\n'%(info_temp))
                print(cnt)
        indexOut.close()
    
'''
    遍历分词
'''
def DepartWord():
    print(r'D:\Python_M\Src\LRC\IndexLrc.txt')
    # 文件读取
    with open(r'D:\Python_M\Src\LRC\IndexLrc.txt',encoding='utf-8',mode='r') as lrcIndex:
        alrc = lrcIndex.readlines()
        lrcIndex.close()
    cnt = 0
    index_prt = rd.randint(100,200)
    for i in alrc:
        cnt += 1
        if cnt == index_prt:
            cur_i = i.strip('\n')
            print(cur_i)
            PrintPiece(cur_i)


# 处理单个文件
def PrintPiece(file):
    final_text = ""
    if os.path.isfile(file):
        print(file)
        with open(file,encoding='utf-8',mode='r') as curfile:
            aline = curfile.readlines()
            # print(aline)
        curfile.close()
        for j in aline:
            # print(j)
            # re
            if isinstance(j,str):
                # remove time table
                OutCut = ['：']
                piece_pattern = re.compile(r"\[.+\]")
                words = piece_pattern.sub(" ",j)
                words = words.strip()
                # remove words contains "："
                if len(words) > 0 and words.find("：") == -1:
                    seg_list = jieba.cut(words)
                    print(words)
                    print(seg_list)
                    LineSplit = ""
                    LineSplit +=  " ".join(seg_list)
                    print("Full Mode: " +  LineSplit) # full modle
                    final_text += LineSplit
        GetCloud(final_text)
        return  final_text
    else:
        print('input is not a file')
        return ""

# test for remove "："
def Remove_R1():
    egs = "：remove"
    print(egs)
    a = egs.find("：")
    print(a)

# word cloud
def GetCloud(src_text):
    if isinstance(src_text,str):
        wc = WordCloud(
            background_color="white", #背景颜色
            max_words=200, #显示最大词数
            font_path="C:\\Windows\\Fonts\\STSONG.TTF",  #使用字体
            min_font_size=15,
            max_font_size=50, 
            width=400  #图幅宽度
            )
        wc.generate(src_text)
        wc.to_file("D:\\Python_M\\Code\\pic.png")
        print("word cloud draw finished + file:D:\\Python_M\\Code\\pic.png")
    else:
        print("not string instance")

def TurtleFig():
    #SquareSpiral1.py
    
    t = turtle.Pen()
    turtle.bgcolor("black")
    sides=eval(input("输入要绘制的边的数目，请输入2-6的数字！"))
    colors=["red","yellow","green","blue","orange","purple"]
    for x in range(100):
        t.pencolor(colors[x%sides])
        t.forward(x*3/sides+x)
        t.left(360/sides+1)
        t.width(x*sides/200)


if __name__ == "__main__":
    os.system("cls")
    print('at least there is a syntax')
    # GetLrc()
    # GetFileIndex()
    # DepartWord()
    # GetCloud("wh ,s ,sdf")
    TurtleFig()

    