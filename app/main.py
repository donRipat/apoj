from time import localtime, strftime
from pydub import AudioSegment
import os

def is_mp3(filename):
    if filename[-4:] == ".mp3":
        return True
    return False

def find_any_mp3(filenames):
    for filename in filenames:
        if is_mp3(filename):
            return filename

print(strftime("%H-%M-%S: shit started\n", localtime()))

intro_name = find_any_mp3(os.listdir("/intro"))
intro = AudioSegment.from_file(f"/intro/{intro_name}", format="mp3")

outro_name = find_any_mp3(os.listdir("/outro"))
outro = AudioSegment.from_file(f"/outro/{outro_name}", format="mp3")

delimiter_name = find_any_mp3(os.listdir("/delimiter"))
delimiter = AudioSegment.from_file(f"/delimiter/{delimiter_name}", format="mp3")

samples = os.listdir("/samples")

final_apoj = AudioSegment.empty()

for sample in samples:
    if not is_mp3(sample):
        print(f"sample = {sample} is not mp3")
        continue
    sound = AudioSegment.from_file(f"/samples/{sample}", format="mp3")
    reversed_sound = sound.reverse()
    if len(final_apoj) != 0:
        final_apoj += delimiter
    final_apoj += reversed_sound + sound

final_apoj = intro + final_apoj + outro
final_apoj.export("/app/apoj.mp3", format="mp3")

print(strftime("\n%H-%M-%S: shit done", localtime()))
