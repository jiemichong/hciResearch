import sounddevice as sd
from scipy.io.wavfile import write

duration = 5  # seconds
fs = 44100
sd.default.samplerate = fs
sd.default.channels = 1 #since macbook input is channel 1
print("Now recording:")
myrecording = sd.rec(duration * fs, blocking=True)
print("Recording is over!")
write('output.wav', fs, myrecording) #write the recording to the file named output.wav

#Running the program: python recorder.py