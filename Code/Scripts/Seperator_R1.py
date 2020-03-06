# -*- coding:utf-8 -*-
import os

from spleeter.separator import Separator
from spleeter.audio.adapter import get_default_audio_adapter


if __name__ == "__main__":
    separator = Separator('spleeter:2stems')
    src = "D:\\Codes\\Python_M\\Code\\Scripts\\audio_example.mp3"
    des = "D:\\Codes\\Python_M\\Code\\Scripts"
    separator.separate_to_file(src, des, synchronous=False)
