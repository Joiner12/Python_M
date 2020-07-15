# -*- coding:utf-8 -*-

__author__ = 'Risky Jr'

'''
    Generate excutable file
'''
import PyInstaller.__main__ as PyRun
import os
import PathManager
from datetime import datetime


def GenerateExe(startOrnot):
    os.system("chcp 65001")
    # 开始
    if startOrnot:
        ExeNumber = 5

        if ExeNumber == 1:
            PyRun.run([
                '--name=%s' % r'PyTick',
                '--onefile',
                '--distpath=%s' % PathManager.GetExePath(),
                '--icon=%s' % os.path.join(
                    PathManager.GetUiPath(), 'Deer.ico'),
                '--noconsole',
                '--clean',
                # '--exclude-module=[numpy]',
                os.path.join(
                    PathManager.GetScriptPath(), 'PyTick.py'),
            ])
        elif ExeNumber == 2:
            PyRun.run([
                '--name=%s' % r'ColorPicker',
                '--onefile',
                '--distpath=%s' % PathManager.GetExePath(),
                '--icon=%s' % os.path.join(PathManager.GetUiPath(),
                                           'clock-1.ico'),
                '--noconsole',
                os.path.join(
                    PathManager.GetScriptPath(), 'ColorSelect_R1.py'),
            ])
        elif ExeNumber == 3:
            PyRun.run([
                '--distpath=%s' % PathManager.GetExePath(),
                '--workpath=%s' % PathManager.GetExePath(),
                '--name=%s' % r'PyTick',
                '--onedir',
                '--distpath=%s' % PathManager.GetExePath(),
                '--icon=%s' % os.path.join(
                    PathManager.GetUiPath(), 'Deer.ico'),
                '--noconsole',
                '--clean',
                os.path.join(
                    PathManager.GetScriptPath(), 'PyTick.py'),
            ])
            # clock
        elif ExeNumber == 4:
            a = datetime.now()
            b = a.strftime("%H-%M")
            name = 'I-Clock-Ver' + b
            PyRun.run([
                '--name=%s' % name,
                '--onefile',
                '--distpath=%s' % PathManager.GetExePath(),
                '--icon=%s' % os.path.join(
                    PathManager.GetUiPath(), r'I-1.ico'),
                '--noconsole',
                '--workpath=%s' % PathManager.GetExePath(),
                '--specpath=%s' % PathManager.GetExePath(),
                '--clean',
                os.path.join(
                    PathManager.GetScriptPath(), 'Clock_R2.py'),
            ])
        elif ExeNumber == 5:
            a = datetime.now()
            b = a.strftime("%H-%M")
            name = 'I-Clock-Ver' + b
            PyRun.run([
                '--name=%s' % name,
                '--onefile',
                '--distpath=%s' % PathManager.GetExePath(),
                '--icon=%s' % os.path.join(
                    PathManager.GetUiPath(), r'I-1.ico'),
                '--noconsole',
                '--workpath=%s' % PathManager.GetExePath(),
                '--specpath=%s' % PathManager.GetExePath(),
                '--clean',
                os.path.join(
                    PathManager.GetScriptPath(), 'Clock_R3.py'),
            ])

        elif ExeNumber == 6:
            a = datetime.now()
            b = a.strftime("%H-%M")
            name = 'Rolutte-Ver' + b
            PyRun.run([
                '--name=%s' % name,
                '--onefile',
                '--distpath=%s' % PathManager.GetExePath(),
                # '--icon=%s' % os.path.join(
                #     PathManager.GetUiPath(), r'love.png'),
                '--noconsole',
                '--workpath=%s' % PathManager.GetExePath(),
                '--specpath=%s' % PathManager.GetExePath(),
                '--clean',
                os.path.join(
                    PathManager.GetScriptPath(), 'Rolutte.py'),
            ])

        elif ExeNumber == 7:
            a = datetime.now()
            b = a.strftime("%H-%M")
            name = 'Reader' + b
            PyRun.run([
                '--name=%s' % name,
                '--onefile',
                '--distpath=%s' % PathManager.GetExePath(),
                # '--icon=%s' % os.path.join(
                #     PathManager.GetUiPath(), r'love.png'),
                '--noconsole',
                '--workpath=%s' % PathManager.GetExePath(),
                '--specpath=%s' % PathManager.GetExePath(),
                '--clean',
                os.path.join(
                    PathManager.GetScriptPath(), 'Reading.py'),
            ])
        else:
            PyRun.run([
                '--name=%s' % r'Shakehand',
                '--onefile',
                '--distpath=%s' % PathManager.GetExePath(),
                '--icon=%s' % os.path.join(PathManager.GetUiPath(),
                                           'clock-1.ico'),
                '--noconsole',
                os.path.join(
                    PathManager.GetScriptPath(), 'KeyMouse_R1.py'),
            ])
    # 取消
    else:
        print("cancle")


if __name__ == "__main__":
    print("Generate excutable file")
    # G_Start = input('start to generate y|n...\t')
    # GenerateExe(G_Start.strip() == "Y" or G_Start.strip() == "y")
    GenerateExe(True)
