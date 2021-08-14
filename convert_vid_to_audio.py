import moviepy.editor
import glob
import moviepy.editor
from tkinter.filedialog import *

#video = askopenfilename() 
#path="/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Youtube_video_downloader/Youtube downloads"

#files=os.listdir(path)
cnt=1
for filename in glob.glob('/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Youtube_video_downloader/Youtube downloads/*.3gpp',recursive = True):
    video = moviepy.editor.VideoFileClip(filename)
    print(filename)
    audio = video.audio
    

    audio.write_audiofile("sample"+str(cnt)+".mp3")
    #audio.save('/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Youtube_video_downloader/Youtube downloads')
    cnt=cnt+1
