# -*- coding:utf-8 -*-

'''
    Generate excutable file
'''
import PyInstaller.__main__ as PyRun
import os
import PathManager


def GenerateExe(startOrnot):
    os.system("chcp 65001")
    # 开始
    if startOrnot:
        ExeNumber = 1

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
                '--clean',
                # '--exclude-module = [%s]' % ('numpy'),
                os.path.join(
                    PathManager.GetScriptPath(), 'ColorSelect_R1.py'),
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
