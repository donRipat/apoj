import time
from time import localtime, strftime
from pydub import AudioSegment

sound = AudioSegment.from_file("samples/shit.mp3", format="mp3")
reversed_sound = sound.reverse()
nice_try = reversed_sound + sound
nice_try.export("app/apoj.mp3", format="mp3")

print(strftime("%H-%M-%S: shit done\n", localtime()))

