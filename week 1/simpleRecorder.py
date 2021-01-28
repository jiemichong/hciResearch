import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write


#recorder function that records audio and stores as a .wav file
def recorder():
    duration = int(input("Recorder function selected, please input recording duration: "))
    print()
    #duration = 5  # seconds
    fs = 44100
    sd.default.samplerate = fs
    sd.default.channels = 1 #since macbook input is channel 1
    #note: to display list of input/output, type python -m sounddevice

    print("Now recording:")
    myrecording = sd.rec(duration * fs, blocking=True)
    print("Recording is over!")
    write('output.wav', fs, myrecording) #write the recording to the file named output.wav
    return


def playback():
    filename = 'output.wav'
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')  
    print("The audio will start playing now!")
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    print("Thank you for listening!")
    return

def main():
    userOption = 0
    while userOption != 3:
        userOption = int(input("What do you want to do?\n1) Record Audio\n2) Play Audio\n3) Quit app\n"))
        
        if userOption == 1:
            recorder()
        elif userOption == 2:
            playback()
        elif userOption == 3:
            print("Thank you!\n")
            break
        
main()