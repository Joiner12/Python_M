# -*- coding:utf-8 -*-

'''
    Generate excutable file
'''
import PyInstaller.__main__ as PyRun
import os


def GenerateExe(startOrnot):
    # 开始
    if startOrnot:
        ExeNumber = 1
        if ExeNumber == 1:
            PyRun.run([
                '--name=%s' % r'PyTick',
                '--onefile',
                '--distpath=%s' % r'D:\Codes\Python_M\Code\PyTick\Exe',
                '--icon=%s' % os.path.join(r'D:\Codes\Python_M\Code\PyTick\Src',
                                           'Deer.ico'),
                '--noconsole',
                os.path.join(
                    r'D:\Codes\Python_M\Code\PyTick\Scripts', 'PyTick.py'),
            ])
        elif ExeNumber == 2:
            PyRun.run([
                '--name=%s' % r'ColorPicker',
                '--onefile',
                '--distpath=%s' % r'D:\Codes\Python_M\Code\PyTick\Exe',
                '--icon=%s' % os.path.join(r'D:\Codes\Python_M\Code\PyTick\Src',
                                           'clock-1.ico'),
                '--noconsole',
                os.path.join(
                    r'D:\Codes\Python_M\Code\PyTick\Scripts', 'ColorSelect_R1.py'),
            ])
        else:
            pass
    # 取消
    else:
        print("cancle")


if __name__ == "__main__":
    print("Generate excutable file")
    G_Start = input('start to generate y|n...\t')
    GenerateExe(G_Start.strip() == "Y" or G_Start.strip() == "y")
