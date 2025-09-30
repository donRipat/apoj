from time import localtime, strftime
from pydub import AudioSegment
import os
samples = os.listdir("/samples")
nice_try = AudioSegment.empty()
for sample in samples:
    if sample[-4:] != ".mp3":
        print(f"sample = {sample} is not mp3")
        continue
    sound = AudioSegment.from_file(f"/samples/{sample}", format="mp3")
    reversed_sound = sound.reverse()
    nice_try += reversed_sound + sound
nice_try.export("/app/apoj.mp3", format="mp3")
print(strftime("%H-%M-%S: shit done\n", localtime()))
