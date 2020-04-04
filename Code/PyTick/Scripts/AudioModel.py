# -*- coding:utf-8 -*-
"""
    audio model
"""

import sys
import os
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MultiInputDialog_R1 import MultiInputDialog
import PathManager as pathm
import wave
import pyaudio


class audioModel(QWidget):
    def __init__(self):
        super().__init__()

    # r"D:\Codes\Python_M\Code\PyTick\Src\1.wav"
    def PlayAudio(self, wavfile):
        wf = wave.open(wavfile, "rb")
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        deg = 1
        while True:
            # 从音频流中读取1000个采样数据，data类型为str.注意对音频流的读写都是字符串
            data = wf.readframes(1000)
            if data == "":  # 判断是否结束
                break
            stream.write(data)  # 从wf中读数据，然后写到stream中。就是从文件中读取数据然后写到声卡里

        stream.stop_stream()  # 暂停
        stream.close()  # 关闭
        p.terminate()
