import urllib.request
import re
from pytube import YouTube
import os
import moviepy.editor
import glob
import moviepy.editor
from pydub import AudioSegment
from pydub.playback import play
from pydub import AudioSegment
import os
import glob
import zipfile
import mutagen
from mutagen.mp3 import MP3
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def download_videos(singer_name,num_vids):
    os.mkdir('downloads')
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + singer_name)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    for elem in video_ids:
        num_vids =num_vids-1
        link = "https://www.youtube.com/watch?v=" + elem
        try :
            yt = YouTube(link)
        except:
            print("Network Issue")

        try:
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download('./downloads/')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            
            
        except:
            print("error")

        if num_vids == 0 :
            break
            
      
     

    # You dont need the number of files in the folder, just iterate over them directly using:
    
    audio_files = os.listdir('downloads/')
    print(audio_files)
    cnt=0;
    for file in glob.glob('downloads/*.mp3'):
        #spliting the file into the name and the extension
        print(file)
        
        name, ext = os.path.splitext(file)
        if ext == ".mp3":
           mp3_sound = AudioSegment.from_file(file)
           #rename them using the old name + ".wav"
           mp3_sound.export('downloads/file'+str(cnt)+'.wav', format="wav")
        cnt=cnt+1;
    #path1="/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Youtube_video_downloader/"
    filenames=glob.glob('downloads/*.wav')
   
    x=len(filenames)
    for i in range(0,x):
        audio=AudioSegment.from_file('downloads/file'+str(i)+'.wav')
    
        ffmpeg_extract_subclip('downloads/file'+str(i)+'.wav', 120,audio.duration_seconds , targetname=str(i)+'.wav')
    
    
    merged_file=AudioSegment.empty()
    
    
    
    for filename in glob.glob('*.wav'):
        print(filename)
        sound=AudioSegment.from_file(filename)
        merged_file+=sound

    merged_file.export("merged_final.mp3",format="mp3")
    
    zip_file=zipfile.ZipFile('mashup.zip','w')
    zip_file.write('merged_final.mp3', compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()


            

