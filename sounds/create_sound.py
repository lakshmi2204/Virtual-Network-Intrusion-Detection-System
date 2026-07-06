import wave
import struct
import math

file_name = "alert.wav"

sample_rate = 44100
duration = 1 #seconds
frequency = 800 #beep frequency

wav_file = wave.open(file_name, "w")

wav_file.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))
for i in range(int(duration + sample_rate)):
    value = int(32767.0 * math.sin(2 * math.pi * frequency * i / sample_rate))
    data = struct.pack('<h', value)
    wav_file.writeframesraw(data)

wav_file.close()

print("alert.wav created successfully!")
