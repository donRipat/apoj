import time
from time import localtime, strftime 
time.sleep(120)
from pydub import AudioSegment 

sound = AudioSegment.from_file("shit.mp3", format="mp3") 
reversed_sound = sound.reverse() 
reversed_sound.export("output.mp3", format="mp3")

with open("result", "w") as f:
    f.write(strftime("%H-%M-%S: executed", localtime()) + "\n")

