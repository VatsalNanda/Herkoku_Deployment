import mutagen
from mutagen.mp3 import MP3
import numpy as np
x=[]
n=6
y=n+1
for i in range(1,y):
    audio=MP3("sample"+str(i)+".mp3")
    x.append(audio.info.length)

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

for i in range(1,y):
    
    ffmpeg_extract_subclip("sample"+str(i)+".mp3", 120,x[i-1] , targetname="shorter_audio"+str(i)+".mp3")

