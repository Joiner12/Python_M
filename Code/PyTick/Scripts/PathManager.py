# -*- coding:utf-8 -*-
'''
    file\scritp\src path manager
'''

# constexpr
home_pc = True

# ui


def GetUiPath():
    if not home_pc:
        return r"D:\Python_M\Code\PyTick\Src"
    else:
        return r"D:\Codes\Python_M\Code\PyTick\Src"

# log


def GetLogPath():
    if not home_pc:
        return r"D:\Python_M\Code\PyTick\Log"
    else:
        return r"D:\Codes\Python_M\Code\PyTick\Logs"

# lrc


def GetLrcPath():
    if not home_pc:
        return r"D:\Python_M\Src"
    else:
        return r"D:\Codes\Python_M\Src\LRC"

# exe


def GetExePath():
    if not home_pc:
        return r"D:\Python_M\Code\PyTick\Exe"
    else:
        return r"D:\Codes\Python_M\Code\PyTick\Exe"

# script


def GetScriptPath():
    if not home_pc:
        return r"D:\Python_M\Code\PyTick\Scripts"
    else:
        return r"D:\Codes\Python_M\Code\PyTick\Scripts"

# logfile


def GetLogFile():
    if not home_pc:
        return r"D:\Python_M\Code\PyTick\Logs\log.txt"
    else:
        return r"D:\Codes\Python_M\Code\PyTick\Logs\log.txt"
