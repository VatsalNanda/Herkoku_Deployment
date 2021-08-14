from pydub import AudioSegment
from pydub.playback import play
from pydub import AudioSegment
import os
import glob
#

#Change working directory
#os.chdir(path1)

audio_files = os.listdir()

# You dont need the number of files in the folder, just iterate over them directly using:
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       #rename them using the old name + ".wav"
       mp3_sound.export("{0}.wav".format(name), format="wav")

path1="/Users/vatsalnanda/Desktop/Research Interns and Papers/prashant_singh_rana_sir/Youtube_video_downloader/"
merged_file=AudioSegment.empty()
filenames = glob.glob(path1+'*.wav')
for filename in filenames:
    sound=AudioSegment.from_wav(filename)
    merged_file+=sound

merged_file.export("merged_final.mp3",format="mp3")
