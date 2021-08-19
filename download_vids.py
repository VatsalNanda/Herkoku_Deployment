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
#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def download_videos(singer_name,num_vids):
    startMin = 0
    startSec = 0
    endMin = 2
    endSec = 0

    startTime = startMin*60*1000  +  startSec*1000
    endTime = endMin*60*1000 + endSec*1000
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
            song = AudioSegment.from_file(f'./downloads/{new_file}')
            os.remove(f'./downloads/{new_file}')
            extract = song[startTime:endTime]
            extract.export(f'./downloads/{new_file}', format="mp3")
            
            
            
        except:
            print("error")

        if num_vids == 0 :
            break
            
      
     
    print(os.getcwd())
    filenames_new=os.listdir(f'./downloads/{new_file}')
    print(filenames)
    # You dont need the number of files in the folder, just iterate over them directly using:
    
    
#    audio_files = os.listdir('downloads/')
#    print(audio_files)
#    cnt=0;
#    for file in glob.glob('downloads/*.mp3'):
#        #spliting the file into the name and the extension
#        print(file)
#
#        name, ext = os.path.splitext(file)
#        if ext == ".mp3":
#           mp3_sound = AudioSegment.from_file(file)
#           #rename them using the old name + ".wav"
#           mp3_sound.export('downloads/file'+str(cnt)+'.wav', format="wav")
#        cnt=cnt+1;
#    #path1="/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Youtube_video_downloader/"
#    filenames=glob.glob('downloads/*.wav')
#
#    x=len(filenames)
#    for i in range(0,x):
#        audio=AudioSegment.from_file('downloads/file'+str(i)+'.wav')
#
#        ffmpeg_extract_subclip('downloads/file'+str(i)+'.wav', 120,audio.duration_seconds , targetname=str(i)+'.wav')

    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))
    zip_file = zipfile.ZipFile('songs.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./downloads/', zip_file)
    zip_file.close()
    shutil.rmtree('downloads')

    
    #merged_file=AudioSegment.empty()
#
#
    
#    for filename in glob.glob('/downloads/*.mp3'):
#        print(filename)
#        sound=AudioSegment.from_file(filename)
#        merged_file+=sound
#
#    merged_file.export("merged_final.mp3",format="mp3")
#
#    zip_file=zipfile.ZipFile('mashup.zip','w')
#    zip_file.write('merged_final.mp3', compress_type=zipfile.ZIP_DEFLATED)
#    zip_file.close()



            

