#encoding:utf-8
__author__: "Anonymous"
__date__: "2019-12-5"
import os
import re
import datetime
import random as rd
import jieba

'''
    遍历文件
'''

# 从单个文件中读取
def GetLrc():
    print('get lrc from file')
    file = 'D:\\1874 (Live).lrc'
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
    if os.path.isfile(file):
        print(file)
        with open(file,encoding='utf-8',mode='r') as curfile:
            aline = curfile.readlines()
            # print(aline)
        curfile.close()
        for j in aline:
            # print(j)
            # 正则表达式替换
            if isinstance(j,str):
                # 处理多余信息
                OutCut = ['母带','鼓手','作曲','：']
                piece_pattern = re.compile(r"\[.+\]")
                words = piece_pattern.sub(" ",j)
                if len(words)!=0:
                    # 默认是精确模式 分词
                    seg_list = jieba.cut(words)
                    print(words)
                    print(seg_list)
                    print("Full Mode: " + "/ ".join(seg_list))  # 全模式
                    
    else:
        print('input is not a file')
        return


if __name__ == "__main__":
    os.system("cls")
    print('at least there is a syntax')
    # GetLrc()
    # GetFileIndex()
    DepartWord()

    