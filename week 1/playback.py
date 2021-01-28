import sounddevice as sd
import soundfile as sf

filename = 'output.wav'
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
print("The audio will start playing now!")
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing
print("Thank you for listening!")